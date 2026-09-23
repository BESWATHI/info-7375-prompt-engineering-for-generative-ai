import React from 'react';
import { z } from 'zod';
import { Ch1Stage, CH1, SERIF, SANS, MONO, cue, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainTarget — the beat the whole reel exists for.
 *
 * Two target vectors sit side by side and are held: the one pretraining
 * actually uses (one-hot on the token that FOLLOWED in the text) and the one
 * a truth-seeking objective would use (one-hot on the true continuation).
 * The second is struck out, because nothing in the pretraining objective ever
 * constructs it — there is no place in the loss where world-truth could enter.
 *
 * Comparison is side-by-side and held, per the legibility contract; the
 * struck column stays at 0.55 opacity, never below the ~40% floor.
 */

const Slot = z.object({ token: z.string(), y: z.number() });

export const ch1PretrainTargetSchema = z.object({
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
  durationS: z.number().default(17),
  sparkLine: z.string().default('One-hot on the text.'),
  vocab: z.array(z.string()).default(['rock', 'cheese', 'gas', 'light']),
  /** The token that followed in the corpus — the real target. */
  target: z.string().default('cheese'),
  /** The true continuation — the target a truth objective would want. */
  truth: z.string().default('rock'),
  leftTitle: z.string().default('THE TARGET VECTOR y'),
  leftWhy: z.string().default('because the text said so'),
  rightTitle: z.string().default('A TRUTH VECTOR'),
  rightWhy: z.string().default('pretraining never builds this'),
});
export type Ch1PretrainTargetProps = z.infer<typeof ch1PretrainTargetSchema>;

const Vector: React.FC<{
  vocab: string[];
  hot: string;
  struck: boolean;
  reveal: (i: number) => number;
}> = ({ vocab, hot, struck, reveal }) => (
  <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
    {vocab.map((t, i) => {
      const isHot = t === hot;
      const o = reveal(i);
      return (
        <div key={t} style={{ display: 'flex', alignItems: 'center', gap: 22, opacity: o }}>
          <div
            style={{
              width: 250,
              fontFamily: MONO,
              fontSize: 42,
              color: isHot && !struck ? CH1.SPARK : CH1.INK,
              fontWeight: isHot ? 700 : 500,
              textDecoration: struck ? 'line-through' : 'none',
            }}
          >
            {t}
          </div>
          <div
            style={{
              width: 88,
              height: 88,
              borderRadius: 10,
              border: `4px solid ${isHot && !struck ? CH1.SPARK : CH1.BORDER}`,
              background: isHot && !struck ? CH1.SPARK : CH1.CARD,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontFamily: MONO,
              fontSize: 48,
              fontWeight: 800,
              color: isHot && !struck ? CH1.CARD : CH1.INK_SOFT,
            }}
          >
            {isHot ? '1' : '0'}
          </div>
        </div>
      );
    })}
  </div>
);

export const Ch1PretrainTarget: React.FC<Ch1PretrainTargetProps> = (props) => {
  const p = useBeatProgress();
  const {
    sparkLine, vocab, target, truth, leftTitle, leftWhy, rightTitle, rightWhy,
  } = ch1PretrainTargetSchema.parse(props);

  const leftO = cue(p, 0.04, 0.14);
  const leftRow = (i: number) => cue(p, 0.16 + i * 0.05, 0.26 + i * 0.05);
  const rightO = cue(p, 0.48, 0.58);
  const rightRow = (i: number) => cue(p, 0.52 + i * 0.04, 0.62 + i * 0.04);
  const crossO = cue(p, 0.74, 0.86);

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="CONSTRUCTED EXAMPLE">
      <div style={{ display: 'flex', gap: 60, alignItems: 'stretch' }}>
        {/* ── the vector pretraining uses ── */}
        <div
          style={{
            flex: 1,
            opacity: leftO,
            border: `4px solid ${CH1.SPARK}`,
            borderRadius: 14,
            padding: '32px 36px',
            background: 'rgba(217,119,87,0.06)',
          }}
        >
          <div style={{ fontFamily: SANS, fontSize: 22, fontWeight: 800, letterSpacing: '0.13em', color: CH1.SPARK }}>
            {leftTitle}
          </div>
          <div style={{ fontFamily: SERIF, fontSize: 34, color: CH1.INK, marginTop: 8, marginBottom: 26, fontWeight: 600 }}>
            {leftWhy}
          </div>
          <Vector vocab={vocab} hot={target} struck={false} reveal={leftRow} />
        </div>

        {/* ── the vector nothing builds ── */}
        <div style={{ flex: 1, position: 'relative', opacity: rightO }}>
          <div
            style={{
              border: `4px solid ${CH1.BORDER}`,
              borderRadius: 14,
              padding: '32px 36px',
              opacity: 0.55,
              height: '100%',
              boxSizing: 'border-box',
            }}
          >
            <div style={{ fontFamily: SANS, fontSize: 22, fontWeight: 800, letterSpacing: '0.13em', color: CH1.INK_SOFT }}>
              {rightTitle}
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 34, color: CH1.INK, marginTop: 8, marginBottom: 26, fontWeight: 600 }}>
              {rightWhy}
            </div>
            <Vector vocab={vocab} hot={truth} struck reveal={rightRow} />
          </div>

          {/* the cross-out — drawn on, not faded in */}
          <svg
            width="100%"
            height="100%"
            style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}
            preserveAspectRatio="none"
            viewBox="0 0 100 100"
          >
            <line
              x1={2} y1={2} x2={2 + 96 * crossO} y2={2 + 96 * crossO}
              stroke={CH1.WARN} strokeWidth={1.1} strokeLinecap="round" vectorEffect="non-scaling-stroke"
            />
            <line
              x1={98} y1={2} x2={98 - 96 * crossO} y2={2 + 96 * crossO}
              stroke={CH1.WARN} strokeWidth={1.1} strokeLinecap="round" vectorEffect="non-scaling-stroke"
            />
          </svg>
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainTargetDemoDefaultProps: Ch1PretrainTargetProps =
  ch1PretrainTargetSchema.parse({});
