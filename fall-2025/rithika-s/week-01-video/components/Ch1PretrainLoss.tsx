import React from 'react';
import { z } from 'zod';
import { Ch1Stage, CH1, SERIF, SANS, MONO, cue, remap, clamp, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainLoss — cross-entropy, and the one slot it reads.
 *
 * L = -ln p(target). The sum over the vocabulary collapses to a single term,
 * because y is one-hot — so every probability except the target's is
 * multiplied by zero and leaves the expression. That collapse is the
 * mechanism: there is no term in the loss that world-truth could occupy.
 *
 * The counterfactual panel is the honesty move. Had the corpus said "rock",
 * the identical forward pass would have scored 0.0762 nats instead of 3.0762.
 * Nothing about the model changed between the two panels — only the text did.
 *
 * The strip at the bottom states the exact identity the two numbers obey:
 *   L(cheese) - L(rock) = z(rock) - z(cheese) = 3.0
 * because ln p_i - ln p_j = z_i - z_j under a shared denominator. Asserted
 * in verify_softmax.py to 1e-12.
 */

export const ch1PretrainLossSchema = z.object({
  /**
   * Beat length in seconds. The reel's MEASURED audio duration is written here
   * by the beat sheet, and calculateMetadata turns it into the composition's
   * frame count — so every reveal in this scene is distributed across the real
   * spoken window instead of a frame count guessed at authoring time.
   *
   * This matters: remotion_scenes.py truncates a rendered clip to the beat's
   * duration (ffmpeg -t). A composition registered LONGER than its audio loses
   * its late reveals silently. See FRICTIONAL.md.
   */
  durationS: z.number().default(24),
  sparkLine: z.string().default('Punished for being right.'),
  target: z.string().default('cheese'),
  truth: z.string().default('rock'),
  pTarget: z.number().default(0.0461),
  pTruth: z.number().default(0.9266),
  lossTarget: z.number().default(3.0762),
  lossTruth: z.number().default(0.0762),
  logitTarget: z.number().default(1.0),
  logitTruth: z.number().default(4.0),
});
export type Ch1PretrainLossProps = z.infer<typeof ch1PretrainLossSchema>;

const Panel: React.FC<{
  eyebrow: string;
  token: string;
  prob: number;
  loss: number;
  accent: boolean;
  fill: number;
  note: string;
}> = ({ eyebrow, token, prob, loss, accent, fill, note }) => {
  const MAX_LOSS = 3.5;   // shared scale, so the two bars are comparable
  return (
    <div
      style={{
        flex: 1,
        border: `4px solid ${accent ? CH1.SPARK : CH1.BORDER}`,
        borderRadius: 14,
        padding: '30px 34px 34px',
        background: accent ? 'rgba(217,119,87,0.06)' : 'transparent',
        opacity: accent ? 1 : 0.7,
        display: 'flex',
        flexDirection: 'column',
        gap: 14,
      }}
    >
      <div style={{ fontFamily: SANS, fontSize: 21, fontWeight: 800, letterSpacing: '0.13em', color: accent ? CH1.SPARK : CH1.INK_SOFT }}>
        {eyebrow}
      </div>
      <div style={{ fontFamily: MONO, fontSize: 34, color: CH1.INK }}>
        L = −ln p(<span style={{ color: accent ? CH1.SPARK : CH1.INK, fontWeight: 700 }}>{token}</span>)
      </div>
      <div style={{ fontFamily: MONO, fontSize: 30, color: CH1.INK_SOFT }}>
        = −ln {prob.toFixed(4)}
      </div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 16, marginTop: 4 }}>
        <span
          style={{
            fontFamily: SERIF,
            fontSize: 132,
            fontWeight: 700,
            lineHeight: 1,
            color: accent ? CH1.SPARK : CH1.INK,
            letterSpacing: '-0.02em',
          }}
        >
          {(loss * fill).toFixed(4)}
        </span>
        <span style={{ fontFamily: SANS, fontSize: 32, color: CH1.INK_SOFT, fontWeight: 600 }}>nats</span>
      </div>
      {/* the penalty as a bar on a shared scale */}
      <div style={{ width: '100%', height: 30, background: '#E4E0D4', borderRadius: 4, overflow: 'hidden' }}>
        <div
          style={{
            width: `${clamp((loss / MAX_LOSS) * fill, 0, 1) * 100}%`,
            height: '100%',
            background: accent ? CH1.SPARK : CH1.INK,
          }}
        />
      </div>
      <div style={{ fontFamily: SANS, fontSize: 25, color: CH1.INK_SOFT, lineHeight: 1.35, marginTop: 2 }}>
        {note}
      </div>
    </div>
  );
};

export const Ch1PretrainLoss: React.FC<Ch1PretrainLossProps> = (props) => {
  const p = useBeatProgress();
  const {
    sparkLine, target, truth, pTarget, pTruth, lossTarget, lossTruth,
    logitTarget, logitTruth,
  } = ch1PretrainLossSchema.parse(props);

  const collapseO = cue(p, 0.02, 0.10);
  const leftO = cue(p, 0.14, 0.24);
  const leftFill = clamp(remap(p, 0.20, 0.40, 0, 1), 0, 1);
  const rightO = cue(p, 0.46, 0.56);
  const rightFill = clamp(remap(p, 0.50, 0.66, 0, 1), 0, 1);
  const stripO = cue(p, 0.76, 0.88);

  const lossGap = lossTarget - lossTruth;
  const logitGap = logitTruth - logitTarget;

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="CONSTRUCTED EXAMPLE">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 26 }}>
        {/* ── the collapse: the sum has one surviving term ── */}
        <div style={{ opacity: collapseO, fontFamily: MONO, fontSize: 34, color: CH1.INK }}>
          L = −Σ y·ln p
          <span style={{ color: CH1.INK_SOFT, margin: '0 18px' }}>→</span>
          <span style={{ color: CH1.SPARK, fontWeight: 700 }}>−ln p({target})</span>
          <span style={{ fontFamily: SANS, fontSize: 27, color: CH1.INK_SOFT, marginLeft: 22 }}>
            every non-target term is multiplied by zero
          </span>
        </div>

        {/* ── same model, two corpora ── */}
        <div style={{ display: 'flex', gap: 44 }}>
          <div style={{ flex: 1, opacity: leftO, display: 'flex' }}>
            <Panel
              eyebrow="THE CORPUS SAID “CHEESE”"
              token={target}
              prob={pTarget}
              loss={lossTarget}
              accent
              fill={leftFill}
              note="This is the gradient the model actually receives."
            />
          </div>
          <div style={{ flex: 1, opacity: rightO, display: 'flex' }}>
            <Panel
              eyebrow="HAD THE CORPUS SAID “ROCK”"
              token={truth}
              prob={pTruth}
              loss={lossTruth}
              accent={false}
              fill={rightFill}
              note="Identical weights, identical forward pass. Only the text differs."
            />
          </div>
        </div>

        {/* ── the exact identity ── */}
        <div
          style={{
            opacity: stripO,
            borderTop: `3px solid ${CH1.INK}`,
            paddingTop: 20,
            display: 'flex',
            alignItems: 'baseline',
            gap: 20,
            flexWrap: 'wrap',
          }}
        >
          <span style={{ fontFamily: SERIF, fontSize: 38, fontWeight: 700, color: CH1.INK }}>
            The whole penalty is the ranking gap:
          </span>
          <span style={{ fontFamily: MONO, fontSize: 36, color: CH1.INK }}>
            {lossTarget.toFixed(4)} − {lossTruth.toFixed(4)} ={' '}
            <span style={{ color: CH1.SPARK, fontWeight: 700 }}>{lossGap.toFixed(1)}</span>
            {'  =  '}
            z({truth}) − z({target}) = {logitTruth.toFixed(1)} − {logitTarget.toFixed(1)}
          </span>
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainLossDemoDefaultProps: Ch1PretrainLossProps =
  ch1PretrainLossSchema.parse({});
