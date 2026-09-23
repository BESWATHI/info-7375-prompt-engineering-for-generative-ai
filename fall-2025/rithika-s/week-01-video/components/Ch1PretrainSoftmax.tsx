import React from 'react';
import { z } from 'zod';
import { Ch1Stage, Ch1Bar, CH1, SERIF, SANS, MONO, cue, clamp, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainSoftmax — exp(z) / Σexp(z), one row at a time, then the proof
 * that the four probabilities sum to exactly 1.0000.
 *
 * The stacked unit bar at the bottom is the argument: the four segments tile
 * the full width with nothing left over. A distribution has to spend all of
 * its mass somewhere, which is why raising p(cheese) must lower p(rock) —
 * the squeeze the loss beat then exploits.
 *
 * Figures asserted in verify_softmax.py (4-dp probabilities sum to exactly
 * 1.0; 1-dp percentages sum to exactly 100.0).
 */

const Row = z.object({
  token: z.string(),
  exp: z.number(),
  p: z.number(),
});

export const ch1PretrainSoftmaxSchema = z.object({
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
  sparkLine: z.string().default('Now they are odds.'),
  rows: z.array(Row).default([
    { token: 'rock', exp: 54.5982, p: 0.9266 },
    { token: 'cheese', exp: 2.7183, p: 0.0461 },
    { token: 'gas', exp: 1.0, p: 0.017 },
    { token: 'light', exp: 0.6065, p: 0.0103 },
  ]),
  expSum: z.number().default(58.923),
  target: z.string().default('cheese'),
});
export type Ch1PretrainSoftmaxProps = z.infer<typeof ch1PretrainSoftmaxSchema>;

const COL = { token: 250, frac: 400, bar: 480, p: 200, pct: 190 } as const;
const GAP = 30;

export const Ch1PretrainSoftmax: React.FC<Ch1PretrainSoftmaxProps> = (props) => {
  const p = useBeatProgress();
  const { sparkLine, rows, expSum, target } = ch1PretrainSoftmaxSchema.parse(props);

  const formulaO = cue(p, 0.02, 0.11);
  const headO = cue(p, 0.11, 0.18);
  const rowAt = (i: number) => cue(p, 0.20 + i * 0.065, 0.31 + i * 0.065);
  const stackO = cue(p, 0.62, 0.72);
  const stackFill = cue(p, 0.66, 0.84);
  const sumO = cue(p, 0.84, 0.93);

  const pSum = rows.reduce((s, r) => s + r.p, 0);
  const pctSum = rows.reduce((s, r) => s + Math.round(r.p * 1000) / 10, 0);
  const STACK_W = 1728;

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="CONSTRUCTED EXAMPLE">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 30 }}>
        {/* ── the formula ── */}
        <div style={{ fontFamily: SERIF, fontSize: 42, color: CH1.INK, opacity: formulaO, fontWeight: 600 }}>
          p(token) = exp(z) ÷ Σ exp(z)
          <span style={{ fontFamily: MONO, fontSize: 30, color: CH1.INK_SOFT, marginLeft: 22 }}>
            Σ = {expSum.toFixed(4)}
          </span>
        </div>

        {/* ── header ── */}
        <div style={{ display: 'flex', gap: GAP, opacity: headO }}>
          <div style={{ width: COL.token, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT }}>CANDIDATE</div>
          <div style={{ width: COL.frac, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT }}>exp(z) ÷ Σ</div>
          <div style={{ width: COL.bar }} />
          <div style={{ width: COL.p, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, textAlign: 'right' }}>p</div>
          <div style={{ width: COL.pct, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, textAlign: 'right' }}>PERCENT</div>
        </div>

        {/* ── rows ── */}
        {rows.map((r, i) => {
          const o = rowAt(i);
          const isTarget = r.token === target;
          return (
            <div key={r.token} style={{ display: 'flex', gap: GAP, alignItems: 'center', opacity: o }}>
              <div style={{ width: COL.token, fontFamily: MONO, fontSize: 46, fontWeight: isTarget ? 700 : 500, color: isTarget ? CH1.SPARK : CH1.INK }}>
                {r.token}
              </div>
              <div style={{ width: COL.frac, fontFamily: MONO, fontSize: 32, color: CH1.INK_SOFT }}>
                {r.exp.toFixed(4)} ÷ {expSum.toFixed(4)}
              </div>
              <div style={{ width: COL.bar }}>
                <Ch1Bar frac={r.p * clamp(o, 0, 1)} width={COL.bar} height={50} accent={isTarget} />
              </div>
              <div style={{ width: COL.p, fontFamily: MONO, fontSize: 44, fontWeight: 700, color: isTarget ? CH1.SPARK : CH1.INK, textAlign: 'right' }}>
                {r.p.toFixed(4)}
              </div>
              <div style={{ width: COL.pct, fontFamily: MONO, fontSize: 40, color: CH1.INK, textAlign: 'right' }}>
                {(Math.round(r.p * 1000) / 10).toFixed(1)}%
              </div>
            </div>
          );
        })}

        {/* ── the unit bar: the mass has to tile exactly ── */}
        <div style={{ opacity: stackO, marginTop: 10 }}>
          <div style={{ display: 'flex', width: STACK_W, height: 78, borderRadius: 5, overflow: 'hidden', border: `3px solid ${CH1.INK}` }}>
            {rows.map((r) => {
              const isTarget = r.token === target;
              return (
                <div
                  key={r.token}
                  style={{
                    width: r.p * STACK_W * stackFill,
                    height: '100%',
                    background: isTarget ? CH1.SPARK : CH1.INK,
                    opacity: isTarget ? 1 : 0.78,
                    borderRight: `2px solid ${CH1.GROUND}`,
                    display: 'flex',
                    alignItems: 'center',
                    paddingLeft: 14,
                    boxSizing: 'border-box',
                    overflow: 'hidden',
                  }}
                >
                  <span style={{ fontFamily: MONO, fontSize: 26, color: CH1.CARD, whiteSpace: 'nowrap', fontWeight: 700 }}>
                    {r.p * STACK_W * stackFill > 190 ? r.token : ''}
                  </span>
                </div>
              );
            })}
          </div>
        </div>

        {/* ── the sum, stated ── */}
        <div style={{ display: 'flex', gap: GAP, alignItems: 'center', opacity: sumO, paddingTop: 6 }}>
          <div style={{ width: COL.token + COL.frac + GAP, fontFamily: SERIF, fontSize: 40, fontWeight: 700, color: CH1.INK }}>
            Σ p
          </div>
          <div style={{ width: COL.bar, fontFamily: SANS, fontSize: 25, color: CH1.INK_SOFT }}>
            no mass left over — exactly
          </div>
          <div style={{ width: COL.p, fontFamily: MONO, fontSize: 48, fontWeight: 700, color: CH1.INK, textAlign: 'right' }}>
            {pSum.toFixed(4)}
          </div>
          <div style={{ width: COL.pct, fontFamily: MONO, fontSize: 44, fontWeight: 700, color: CH1.INK, textAlign: 'right' }}>
            {pctSum.toFixed(1)}%
          </div>
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainSoftmaxDemoDefaultProps: Ch1PretrainSoftmaxProps =
  ch1PretrainSoftmaxSchema.parse({});
