import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { z } from 'zod';
import { CH1, SERIF, SANS, cue, clamp } from './Ch1Chrome';
import { SAFE } from '../tokens/layout';

/**
 * Ch1PretrainTakeaway — Act 6. One sentence, no new claims.
 *
 * The last beat restates the core idea in plain language and stops. It
 * introduces nothing: every phrase here has already been shown as a mechanism
 * earlier in the reel. It also carries the reel's title restate and the course
 * credit rail, so it serves as the outro without a separate card.
 *
 * Anchored to SAFE's top and bottom edges deliberately — a centred poster
 * scored 16% of the safe area on the first pass and failed Gate V, which
 * measures the ink BOUNDING BOX rather than ink density.
 */

export const ch1PretrainTakeawaySchema = z.object({
  durationS: z.number().default(12),
  eyebrow: z.string().default('THE TAKEAWAY'),
  takeaway: z.string().default(
    'Pretraining scores the model against the token that came next in the text — not against what is true.',
  ),
  title: z.string().default('The Token That Followed'),
  handle: z.string().default('INFO 7375 · Prompt Engineering for Generative AI'),
  credit: z.string().default('Rithika Sankar Rajeswari · narrated by Sasha'),
  rail: z.string().default('Kokoro TTS af_bella · Brutalist toolkit · $0.00'),
});
export type Ch1PretrainTakeawayProps = z.infer<typeof ch1PretrainTakeawaySchema>;

const Spark: React.FC<{ size: number }> = ({ size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ flexShrink: 0 }}>
    <path
      d="M12 1.6 L13.9 9.4 L21.2 12 L13.9 14.6 L12 22.4 L10.1 14.6 L2.8 12 L10.1 9.4 Z"
      fill={CH1.SPARK}
    />
  </svg>
);

export const Ch1PretrainTakeaway: React.FC<Ch1PretrainTakeawayProps> = (props) => {
  const { eyebrow, takeaway, title, handle, credit, rail } =
    ch1PretrainTakeawaySchema.parse(props);
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);

  const eyebrowO = cue(p, 0.02, 0.12);
  const lineO = cue(p, 0.06, 0.30);
  const ruleW = cue(p, 0.34, 0.54);
  const titleO = cue(p, 0.46, 0.62);
  const creditO = cue(p, 0.58, 0.74);
  const railO = cue(p, 0.66, 0.82);

  return (
    <AbsoluteFill style={{ background: CH1.GROUND }}>
      {/* top edge of SAFE */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y, width: SAFE.w,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          opacity: eyebrowO,
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <Spark size={30} />
          <span style={{ fontFamily: SANS, fontSize: 27, fontWeight: 800, letterSpacing: '0.14em', color: CH1.INK }}>
            {eyebrow}
          </span>
        </div>
        <span style={{ fontFamily: SANS, fontSize: 25, fontWeight: 700, letterSpacing: '0.12em', color: CH1.INK_SOFT }}>
          INFO 7375 · CH 1
        </span>
      </div>

      {/* the one sentence */}
      <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
        <div
          style={{
            fontFamily: SERIF,
            fontSize: 76,
            fontWeight: 700,
            color: CH1.INK,
            letterSpacing: '-0.02em',
            textAlign: 'center',
            maxWidth: SAFE.w - 60,
            lineHeight: 1.22,
            opacity: lineO,
          }}
        >
          {takeaway.replace(/\.$/, '')}
          <span style={{ color: CH1.SPARK }}>.</span>
        </div>

        <div style={{ width: (SAFE.w - 420) * ruleW, height: 5, background: CH1.SPARK, marginTop: 44, borderRadius: 3 }} />

        <div
          style={{
            fontFamily: SANS, fontSize: 36, fontWeight: 700, color: CH1.INK,
            marginTop: 40, opacity: titleO, textAlign: 'center',
          }}
        >
          {title}
        </div>
      </AbsoluteFill>

      {/* bottom edge of SAFE */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 44, width: SAFE.w,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        }}
      >
        <span style={{ fontFamily: SANS, fontSize: 31, fontWeight: 700, color: CH1.INK, opacity: creditO }}>
          {credit}
        </span>
        <span style={{ fontFamily: SANS, fontSize: 24, color: CH1.INK_SOFT, opacity: railO * 0.9 }}>
          {handle.includes('INFO') ? rail : rail}
        </span>
      </div>
    </AbsoluteFill>
  );
};

export const ch1PretrainTakeawayDemoDefaultProps: Ch1PretrainTakeawayProps =
  ch1PretrainTakeawaySchema.parse({});
