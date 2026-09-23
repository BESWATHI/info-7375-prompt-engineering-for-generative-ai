import React from 'react';
import { z } from 'zod';
import { Ch1Stage, CH1, SERIF, SANS, MONO, cue, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainGradient — where the penalty goes.
 *
 * For softmax + cross-entropy the gradient on the logits is exactly p − y.
 * No approximation, no extra term: subtract the one-hot target from the
 * predicted distribution and you have the update direction.
 *
 * Read down the column and the objective states itself. `cheese` carries
 * −0.9539, so its score is pushed UP. `rock` carries +0.9266, so the true
 * continuation is pushed DOWN — hardest of all the non-targets, precisely
 * because the model believed it most. The column sums to zero (p and y both
 * sum to 1), which is the check that the mass is only ever redistributed.
 *
 * Figures asserted in verify_softmax.py.
 */

const Row = z.object({
  token: z.string(),
  p: z.number(),
  y: z.number(),
});

export const ch1PretrainGradientSchema = z.object({
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
  durationS: z.number().default(18),
  sparkLine: z.string().default('Truth pushed down hardest.'),
  formula: z.string().default('∂L / ∂z = p − y'),
  rows: z.array(Row).default([
    { token: 'rock', p: 0.9266, y: 0 },
    { token: 'cheese', p: 0.0461, y: 1 },
    { token: 'gas', p: 0.017, y: 0 },
    { token: 'light', p: 0.0103, y: 0 },
  ]),
  truth: z.string().default('rock'),
  closingNote: z.string().default(
    'The steepest correction in the batch is aimed at the one true answer.',
  ),
});
export type Ch1PretrainGradientProps = z.infer<typeof ch1PretrainGradientSchema>;

const COL = { token: 260, p: 220, y: 170, g: 300, dir: 330 } as const;
const GAP = 34;

export const Ch1PretrainGradient: React.FC<Ch1PretrainGradientProps> = (props) => {
  const p = useBeatProgress();
  const { sparkLine, formula, rows, truth, closingNote } =
    ch1PretrainGradientSchema.parse(props);

  const formulaO = cue(p, 0.02, 0.11);
  const headO = cue(p, 0.11, 0.19);
  const rowAt = (i: number) => cue(p, 0.21 + i * 0.075, 0.33 + i * 0.075);
  const arrowAt = (i: number) => cue(p, 0.28 + i * 0.075, 0.40 + i * 0.075);
  const sumO = cue(p, 0.70, 0.80);
  const noteO = cue(p, 0.84, 0.94);

  const gradSum = rows.reduce((s, r) => s + (r.p - r.y), 0);

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="CONSTRUCTED EXAMPLE">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 34 }}>
        <div style={{ opacity: formulaO, fontFamily: SERIF, fontSize: 46, fontWeight: 700, color: CH1.INK }}>
          {formula}
          <span style={{ fontFamily: SANS, fontSize: 27, color: CH1.INK_SOFT, marginLeft: 24, fontWeight: 500 }}>
            exact, not an approximation
          </span>
        </div>

        <div style={{ display: 'flex', gap: GAP, opacity: headO }}>
          <div style={{ width: COL.token, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT }}>CANDIDATE</div>
          <div style={{ width: COL.p, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, textAlign: 'right' }}>p</div>
          <div style={{ width: COL.y, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, textAlign: 'right' }}>− y</div>
          <div style={{ width: COL.g, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, textAlign: 'right' }}>= p − y</div>
          <div style={{ width: COL.dir, fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, paddingLeft: 26 }}>THE SCORE MOVES</div>
        </div>

        {rows.map((r, i) => {
          const o = rowAt(i);
          const a = arrowAt(i);
          const g = r.p - r.y;
          const up = g < 0;
          const isTruth = r.token === truth;
          // accent belongs to the target (the one pushed up); the true
          // continuation is marked in the deeper warn step, once.
          const color = up ? CH1.SPARK : isTruth ? CH1.WARN : CH1.INK;
          return (
            <div key={r.token} style={{ display: 'flex', gap: GAP, alignItems: 'center', opacity: o }}>
              <div style={{ width: COL.token, fontFamily: MONO, fontSize: 48, fontWeight: up || isTruth ? 700 : 500, color }}>
                {r.token}
              </div>
              <div style={{ width: COL.p, fontFamily: MONO, fontSize: 40, color: CH1.INK, textAlign: 'right' }}>
                {r.p.toFixed(4)}
              </div>
              <div style={{ width: COL.y, fontFamily: MONO, fontSize: 40, color: CH1.INK_SOFT, textAlign: 'right' }}>
                − {r.y.toFixed(0)}
              </div>
              <div style={{ width: COL.g, fontFamily: MONO, fontSize: 44, fontWeight: 700, color, textAlign: 'right' }}>
                {g > 0 ? '+' : '−'}{Math.abs(g).toFixed(4)}
              </div>
              <div style={{ width: COL.dir, display: 'flex', alignItems: 'center', gap: 14, paddingLeft: 26, opacity: a }}>
                <span style={{ fontFamily: SANS, fontSize: 46, fontWeight: 800, color, lineHeight: 1 }}>
                  {up ? '↑' : '↓'}
                </span>
                <span style={{ fontFamily: SANS, fontSize: 30, fontWeight: 700, color, whiteSpace: 'nowrap' }}>
                  {up ? 'UP' : 'DOWN'}
                </span>
                {isTruth ? (
                  <span style={{ fontFamily: SANS, fontSize: 22, color: CH1.WARN, whiteSpace: 'nowrap', fontWeight: 700 }}>
                    ← the truth
                  </span>
                ) : null}
              </div>
            </div>
          );
        })}

        <div
          style={{
            display: 'flex',
            gap: GAP,
            alignItems: 'center',
            opacity: sumO,
            borderTop: `3px solid ${CH1.INK}`,
            paddingTop: 20,
          }}
        >
          <div style={{ width: COL.token + COL.p + COL.y + GAP * 2, fontFamily: SERIF, fontSize: 38, fontWeight: 700, color: CH1.INK }}>
            Σ (p − y)
          </div>
          <div style={{ width: COL.g, fontFamily: MONO, fontSize: 44, fontWeight: 700, color: CH1.INK, textAlign: 'right' }}>
            {gradSum.toFixed(4)}
          </div>
          <div style={{ width: COL.dir, fontFamily: SANS, fontSize: 25, color: CH1.INK_SOFT, paddingLeft: 26 }}>
            mass moved, never created
          </div>
        </div>

        <div style={{ opacity: noteO, fontFamily: SERIF, fontSize: 40, color: CH1.INK, fontWeight: 600, lineHeight: 1.3 }}>
          {closingNote}
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainGradientDemoDefaultProps: Ch1PretrainGradientProps =
  ch1PretrainGradientSchema.parse({});
