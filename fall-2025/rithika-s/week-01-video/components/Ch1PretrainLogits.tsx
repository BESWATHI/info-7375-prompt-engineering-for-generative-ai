import React from 'react';
import { z } from 'zod';
import { Ch1Stage, Ch1Bar, CH1, SERIF, SANS, MONO, cue, clamp, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainLogits — the raw scores, before anything is a probability.
 *
 * Four candidate tokens get one unnormalized real number each. The bars are
 * drawn from exp(z), not z, because that is what the softmax numerator
 * actually is — showing the exponential is what makes the next beat's
 * lopsided probabilities legible instead of surprising.
 *
 * Every figure here is asserted in verify_softmax.py.
 */

const Row = z.object({
  token: z.string(),
  logit: z.number(),
  exp: z.number(),
});

export const ch1PretrainLogitsSchema = z.object({
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
  sparkLine: z.string().default('Four scores, not yet odds.'),
  context: z.string().default('The moon is made of green'),
  rows: z.array(Row).default([
    { token: 'rock', logit: 4.0, exp: 54.5982 },
    { token: 'cheese', logit: 1.0, exp: 2.7183 },
    { token: 'gas', logit: 0.0, exp: 1.0 },
    { token: 'light', logit: -0.5, exp: 0.6065 },
  ]),
  expSum: z.number().default(58.923),
  /** The token the corpus actually continued with. */
  target: z.string().default('cheese'),
});
export type Ch1PretrainLogitsProps = z.infer<typeof ch1PretrainLogitsSchema>;

const COL = { token: 300, logit: 220, bar: 560, exp: 330 } as const;
const GAP = 34;

export const Ch1PretrainLogits: React.FC<Ch1PretrainLogitsProps> = (props) => {
  const p = useBeatProgress();
  const { sparkLine, context, rows, expSum, target } = ch1PretrainLogitsSchema.parse(props);

  const ctxO = cue(p, 0.03, 0.12);
  const headO = cue(p, 0.12, 0.20);
  const rowAt = (i: number) => cue(p, 0.22 + i * 0.07, 0.34 + i * 0.07);
  const expColO = cue(p, 0.56, 0.66);
  const sumO = cue(p, 0.74, 0.84);

  const maxExp = Math.max(...rows.map((r) => r.exp));

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="CONSTRUCTED EXAMPLE">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 38 }}>
        {/* ── the context being conditioned on ── */}
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 18, opacity: ctxO }}>
          <span style={{ fontFamily: MONO, fontSize: 38, color: CH1.INK }}>
            &ldquo;{context}&rdquo;
          </span>
          <span style={{ fontFamily: SANS, fontSize: 34, color: CH1.SPARK, fontWeight: 800 }}>→ ?</span>
        </div>

        {/* ── header ── */}
        <div style={{ display: 'flex', gap: GAP, opacity: headO, alignItems: 'flex-end' }}>
          <div style={{ width: COL.token, fontFamily: SANS, fontSize: 21, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT }}>
            CANDIDATE
          </div>
          <div style={{ width: COL.logit, fontFamily: SANS, fontSize: 21, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, textAlign: 'right' }}>
            LOGIT z
          </div>
          <div style={{ width: COL.bar, fontFamily: SANS, fontSize: 21, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT }}>
            exp(z) — THE SOFTMAX NUMERATOR
          </div>
          <div style={{ width: COL.exp, fontFamily: SANS, fontSize: 21, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, textAlign: 'right' }}>
            exp(z)
          </div>
        </div>

        {/* ── rows ── */}
        {rows.map((r, i) => {
          const o = rowAt(i);
          const isTarget = r.token === target;
          return (
            <div key={r.token} style={{ display: 'flex', gap: GAP, alignItems: 'center', opacity: o }}>
              <div
                style={{
                  width: COL.token,
                  fontFamily: MONO,
                  fontSize: 50,
                  fontWeight: isTarget ? 700 : 500,
                  color: isTarget ? CH1.SPARK : CH1.INK,
                }}
              >
                {r.token}
              </div>
              <div
                style={{
                  width: COL.logit,
                  fontFamily: MONO,
                  fontSize: 50,
                  fontWeight: 700,
                  color: CH1.INK,
                  textAlign: 'right',
                }}
              >
                {r.logit > 0 ? '+' : ''}{r.logit.toFixed(1)}
              </div>
              <div style={{ width: COL.bar }}>
                <Ch1Bar
                  frac={(r.exp / maxExp) * clamp(o, 0, 1)}
                  width={COL.bar}
                  height={56}
                  accent={isTarget}
                />
              </div>
              <div
                style={{
                  width: COL.exp,
                  fontFamily: MONO,
                  fontSize: 48,
                  color: CH1.INK,
                  textAlign: 'right',
                  opacity: expColO,
                }}
              >
                {r.exp.toFixed(4)}
              </div>
            </div>
          );
        })}

        {/* ── the denominator ── */}
        <div
          style={{
            display: 'flex',
            gap: GAP,
            alignItems: 'center',
            opacity: sumO,
            borderTop: `3px solid ${CH1.INK}`,
            paddingTop: 22,
          }}
        >
          <div style={{ width: COL.token + COL.logit + GAP, fontFamily: SERIF, fontSize: 40, fontWeight: 700, color: CH1.INK }}>
            Σ exp(z)
          </div>
          <div style={{ width: COL.bar, fontFamily: SANS, fontSize: 26, color: CH1.INK_SOFT }}>
            the denominator every probability is divided by
          </div>
          <div style={{ width: COL.exp, fontFamily: MONO, fontSize: 48, fontWeight: 700, color: CH1.INK, textAlign: 'right' }}>
            {expSum.toFixed(4)}
          </div>
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainLogitsDemoDefaultProps: Ch1PretrainLogitsProps =
  ch1PretrainLogitsSchema.parse({});
