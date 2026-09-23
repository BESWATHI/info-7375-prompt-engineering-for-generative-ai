import React from 'react';
import { z } from 'zod';
import { Ch1Stage, CH1, SERIF, SANS, cue, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainBoundary — NAME THE BOUNDARY.
 *
 * The falsifiability beat. Everything shown up to here is a claim about ONE
 * objective on ONE constructed line, and this card states plainly what that
 * does not buy: it says nothing about post-training, nothing about whether
 * models end up accurate, and nothing measured about any real system.
 *
 * Rendered as a ruled list so the limits read as commitments, not hedging.
 * The banner is dropped here — this beat shows no constructed figures, it
 * describes the construction's edges.
 */

export const ch1PretrainBoundarySchema = z.object({
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
  sparkLine: z.string().default('Where the claim stops.'),
  heading: z.string().default('What this does not establish'),
  items: z.array(z.string()).default([
    'How post-training — preference tuning, RLHF — later steers the model away from raw corpus mimicry and toward factual accuracy. That is a different objective with a different target, and none of its machinery appeared here.',
    'That models must therefore be wrong. Most of a real corpus is broadly true, so mimicry and accuracy agree almost everywhere; this example is built from the case where they come apart.',
    'Anything measured. The corpus line, the four-token vocabulary, and the logits are constructed teaching values — chosen to make the arithmetic legible, not observed from a trained model.',
  ]),
  footer: z.string().default('Only the arithmetic is load-bearing. It is reproducible: verify_softmax.py'),
});
export type Ch1PretrainBoundaryProps = z.infer<typeof ch1PretrainBoundarySchema>;

export const Ch1PretrainBoundary: React.FC<Ch1PretrainBoundaryProps> = (props) => {
  const p = useBeatProgress();
  const { sparkLine, heading, items, footer } = ch1PretrainBoundarySchema.parse(props);

  const headO = cue(p, 0.03, 0.13);
  const itemAt = (i: number) => cue(p, 0.18 + i * 0.16, 0.32 + i * 0.16);
  const footO = cue(p, 0.82, 0.93);

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 34 }}>
        <div
          style={{
            fontFamily: SERIF,
            fontSize: 80,
            fontWeight: 700,
            color: CH1.INK,
            letterSpacing: '-0.02em',
            opacity: headO,
            lineHeight: 1.05,
          }}
        >
          {heading}
          <span style={{ color: CH1.SPARK }}>.</span>
        </div>

        {items.map((t, i) => (
          <div
            key={i}
            style={{
              display: 'flex',
              gap: 26,
              opacity: itemAt(i),
              borderTop: `2px solid ${CH1.BORDER}`,
              paddingTop: 20,
            }}
          >
            <div
              style={{
                fontFamily: SANS,
                fontSize: 30,
                fontWeight: 800,
                color: CH1.SPARK,
                minWidth: 46,
                lineHeight: 1.3,
              }}
            >
              {String(i + 1).padStart(2, '0')}
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 38, color: CH1.INK, lineHeight: 1.4, maxWidth: 1560 }}>
              {t}
            </div>
          </div>
        ))}

        <div
          style={{
            fontFamily: SANS,
            fontSize: 27,
            color: CH1.INK_SOFT,
            opacity: footO,
            paddingTop: 8,
            fontWeight: 600,
          }}
        >
          {footer}
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainBoundaryDemoDefaultProps: Ch1PretrainBoundaryProps =
  ch1PretrainBoundarySchema.parse({});
