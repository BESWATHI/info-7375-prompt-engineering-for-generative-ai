import React from 'react';
import { z } from 'zod';
import { Ch1Stage, Ch1Token, CH1, SERIF, SANS, MONO, cue, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainCorpus — the setup beat.
 *
 * Shows the ONE thing pretraining actually gets: a line of text. The line is
 * deliberately false about the world ("The moon is made of green cheese"),
 * drawn from a constructed science-fiction corpus, so that "what the text
 * says" and "what is true" come apart on screen before any math appears.
 *
 * The move: the full sentence lands -> the context dims -> `green` takes the
 * accent -> the next slot opens as a dashed question mark. The viewer sees the
 * supervision signal being constructed, not asserted.
 */

export const ch1PretrainCorpusSchema = z.object({
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
  sparkLine: z.string().default('The text is the target.'),
  sourceLabel: z.string().default('CONSTRUCTED CORPUS · SCIENCE-FICTION NOVEL, CH. 4'),
  /** The corpus line, space-separated. One token per word for this reel. */
  line: z.string().default('The moon is made of green cheese'),
  /** Index of the conditioning token that takes the accent. */
  focusIndex: z.number().int().default(4),
  truthNote: z.string().default('The real moon is rock.'),
  corpusNote: z.string().default('The corpus says cheese.'),
});
export type Ch1PretrainCorpusProps = z.infer<typeof ch1PretrainCorpusSchema>;

export const Ch1PretrainCorpus: React.FC<Ch1PretrainCorpusProps> = (props) => {
  const p = useBeatProgress();
  const { sparkLine, sourceLabel, line, focusIndex, truthNote, corpusNote } =
    ch1PretrainCorpusSchema.parse(props);

  const tokens = line.split(/\s+/).filter(Boolean);
  const lastIndex = tokens.length - 1;

  // ── Timeline ──
  const cardO = cue(p, 0.03, 0.14);
  const srcO = cue(p, 0.08, 0.18);
  // Tokens type on one at a time across the first third.
  const tokenAt = (i: number) => cue(p, 0.16 + i * 0.035, 0.22 + i * 0.035);
  // Then the split: context recedes, `green` lights, the slot opens.
  const splitP = cue(p, 0.50, 0.62);
  const slotP = cue(p, 0.62, 0.74);
  const notesP = cue(p, 0.78, 0.90);

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="CONSTRUCTED EXAMPLE">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 56 }}>
        {/* ── the corpus card ── */}
        <div
          style={{
            background: CH1.CARD,
            border: `3px solid ${CH1.BORDER}`,
            borderRadius: 14,
            padding: '48px 54px 58px',
            opacity: cardO,
          }}
        >
          <div
            style={{
              fontFamily: SANS,
              fontSize: 26,
              fontWeight: 800,
              letterSpacing: '0.13em',
              color: CH1.INK_SOFT,
              opacity: srcO,
              marginBottom: 30,
            }}
          >
            {sourceLabel}
          </div>

          <div
            style={{
              display: 'flex',
              flexWrap: 'wrap',
              alignItems: 'center',
              gap: 14,
            }}
          >
            {tokens.map((t, i) => {
              const isFocus = i === focusIndex;
              const isTarget = i === lastIndex;
              // Context tokens recede; the focus token stays lit; the final
              // token is lifted out of the sentence and becomes the slot.
              const recede = i < focusIndex ? 1 - splitP * (1 - CH1.DIM) : 1;
              if (isTarget) {
                return (
                  <span key={i} style={{ display: 'inline-flex', opacity: tokenAt(i) }}>
                    {/* the target token fades out as the dashed slot opens */}
                    <span style={{ opacity: 1 - slotP, position: slotP > 0.98 ? 'absolute' : 'static' }}>
                      <Ch1Token text={t} state="rest" fontSize={78} />
                    </span>
                    <span style={{ opacity: slotP }}>
                      <Ch1Token text="?" state="slot" fontSize={78} />
                    </span>
                  </span>
                );
              }
              return (
                <span key={i} style={{ opacity: tokenAt(i) * recede }}>
                  <Ch1Token
                    text={t}
                    state={isFocus && splitP > 0.4 ? 'focus' : 'rest'}
                    fontSize={78}
                  />
                </span>
              );
            })}
          </div>
        </div>

        {/* ── the two readings, side by side, held ── */}
        <div style={{ display: 'flex', gap: 28, opacity: notesP }}>
          <div
            style={{
              flex: 1,
              border: `3px solid ${CH1.SPARK}`,
              borderRadius: 12,
              padding: '36px 40px',
              background: 'rgba(217,119,87,0.07)',
            }}
          >
            <div style={{ fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.SPARK }}>
              WHAT PRETRAINING SEES
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 54, color: CH1.INK, marginTop: 16, fontWeight: 600 }}>
              {corpusNote}
            </div>
          </div>
          <div
            style={{
              flex: 1,
              border: `3px solid ${CH1.BORDER}`,
              borderRadius: 12,
              padding: '36px 40px',
              opacity: 0.72,
            }}
          >
            <div style={{ fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT }}>
              WHAT IS TRUE
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 54, color: CH1.INK, marginTop: 16, fontWeight: 600 }}>
              {truthNote}
            </div>
            <div style={{ fontFamily: MONO, fontSize: 26, color: CH1.INK_SOFT, marginTop: 14 }}>
              never shown to the model
            </div>
          </div>
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainCorpusDemoDefaultProps: Ch1PretrainCorpusProps =
  ch1PretrainCorpusSchema.parse({});
