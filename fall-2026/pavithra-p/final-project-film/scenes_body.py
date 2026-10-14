# ═════════════════════════════ DryRun pitch film v4: scenes ═════════════════════════════
# Body of scenes.py. build_scenes.py writes scenes.py = iso_kit.py + iso_originals_25.py + this file,
# because Gate A copies only scenes.py.
#
# v2 follows my Week 1 film: a course kicker top-left, short phrases (3-10 words) that appear when they
# are spoken, honesty chips (REAL / TESTED / CONSTRUCTED), source footers, and drawings only where they
# explain the mechanism (file ages, folder -> copy, the decision gate, the report card). Colours stay
# beige / ink / terracotta; terracotta is used only for small lights on objects, never for text.
#
# Timing: Clock places each cue where its phrase is spoken (character share of the narration, with
# pauses at punctuation, as in Week 1), keeps every animation out of the 0.6 s window around the clip
# midpoint (where GATE T and Gate V sample), and never runs past the measured audio.

FONT = "Helvetica Neue"
MONO = "Menlo"
OVERS = 4                      # render text 4x and scale down: fixes Manim's small-text kerning (Week 1)
KICKER = "INFO 7375 · DRYRUN · FINAL PROJECT PITCH"
CHIP = "#E6DED2"               # within 28/channel of the stage, so Gate V does not count it as ink
CARD_EDGE = "#B39A72"          # kraft edge, lighter than GATE T's text threshold
MAXW = 11.8


def P(s, size=38, bold=False, font=FONT, color=INK):
    """One line of text. Rendered at OVERS x and scaled down (Week 1's kerning fix); if Pango would wrap
    the oversized line, fall back to a smaller multiplier so the phrase always stays on one line."""
    for ov in (OVERS, 3, 2, 1):
        t = Text(s, font=font, font_size=size * ov, color=color, weight="BOLD" if bold else "NORMAL")
        t.scale_to_fit_width(t.width / ov)
        h = t.height
        if not isinstance(h, (int, float)) or h <= 0.019 * size:
            break
    if t.width > MAXW:
        t.scale_to_fit_width(MAXW)
    return t


def prop(pid, h, x, y):
    return no_terra(make_original(pid, height=h, x=x, y=y), pid)


def no_terra(m, pid):
    """v4: drop the props' terracotta lights. Pavithra asked for no orange dots anywhere in the film.
    Uses the prop data (shape order = submobject order), so Gate A's stub objects pass through."""
    for name, shapes in _ST_ORIGINALS_25[pid]["parts"].items():
        part = m.parts[name]
        try:
            for mob in [part.submobjects[i] for i, sh in enumerate(shapes) if sh.get("fill") == TERRA]:
                part.remove(mob)
        except (AttributeError, IndexError, TypeError):
            pass
    return m


def open_crate(h, x, y):
    """The context crate without its lid, so the files inside show: 'your folder' and its copy."""
    m = prop("context-crate", h, x, y)
    m.remove(m.parts["lid"])
    m.parts["context"].shift(UP * m.parts["crate-front"].height * 0.45)   # files stick up out of the box
    return m.move_to([x, y, 0])


def terminal(cmd, x, y, w=4.0, h=0.78):
    """A small terminal window: light card, dark title bar with three dots, the command in mono."""
    bar = Rectangle(width=w, height=0.16, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([x, y + h / 2 - 0.08, 0])
    dots = VGroup(*[Circle(radius=0.035, fill_color=CHIP, fill_opacity=1, stroke_width=0)
                    .move_to([x - w / 2 + 0.16 + 0.13 * i, y + h / 2 - 0.08, 0]) for i in range(3)])
    t = P(cmd, 22, font=MONO).move_to([x, y - 0.08, 0])
    return VGroup(card(w, h, x, y), bar, dots, t)


def at_xy(m, x, y):
    return m.move_to([x, y, 0])


def chip(s, x, y, size=28, font=FONT, bold=True):
    t = P(s, size, bold=bold, font=font)
    r = RoundedRectangle(width=t.width + 0.5, height=t.height + 0.34, corner_radius=0.12,
                         fill_color=CHIP, fill_opacity=1, stroke_width=0)
    g = VGroup(r, t)
    g.move_to([x, y, 0])
    return g


def card(w, h, x, y):
    shadow = Rectangle(width=w, height=h, fill_color=BOX_TOP, fill_opacity=1, stroke_width=0).move_to([x + 0.08, y - 0.08, 0])
    face = Rectangle(width=w, height=h, fill_color=CARD, fill_opacity=1, stroke_color=CARD_EDGE, stroke_width=2).move_to([x, y, 0])
    return VGroup(shadow, face)


def rule(y, half=3.0):
    return Line([-half, y, 0], [half, y, 0], color=INK, stroke_width=3)


def chrome(scene, footer=None):
    k = P(KICKER, 26)
    k.move_to([-6.1 + k.width / 2, 3.08, 0])
    scene.add(k)
    if footer:
        f = P(footer, 26)
        f.move_to([6.1 - f.width / 2, -3.05, 0])
        scene.add(f)


def _w(s):
    return len(s) + 6 * s.count(".") + 3 * s.count(",") + 4 * s.count(":") + 6 * s.count("?")


class Clock:
    def __init__(self, scene):
        self.s = scene
        bid = type(scene).__name__.split("_")[0]
        self.d = _TARGET.get(bid, 0)
        self.n = _NARR.get(bid, "")
        self.t = 0.0

    def wait(self, x):
        if x > 0.02:
            self.s.wait(x)
            self.t += x

    def play(self, *anims, rt=0.45):
        if self.d:
            lo, hi = self.d / 2 - 0.3, self.d / 2 + 0.3
            if self.t < hi and self.t + rt > lo:
                self.wait(hi - self.t)
            rt = max(0.2, min(rt, self.d - 0.12 - self.t))
        self.s.play(*anims, run_time=rt)
        self.t += rt

    def at(self, phrase, lead=0.15):
        i = self.n.find(phrase)
        if i < 0 or not self.d:
            return
        self.wait(self.d * _w(self.n[:i]) / _w(self.n) - lead - self.t)

    def finish(self):
        self.wait(max(self.d - 0.06 - self.t, 0.05) if self.d else 1.0)


def up(m):
    return FadeIn(m, shift=UP * 0.12)


# ─────────────────────────────────────────── scenes ───────────────────────────────────────────

class B00_Intro(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("Pavithra Prasad", 64, bold=True), 0, 1.7)))
        c.at("and I'm aiming")
        c.play(up(at_xy(P("Target role: backend and platform engineering", 36), 0, 0.75)))
        c.at("Dry Run will be")
        c.play(Create(rule(0.0)), up(at_xy(P("DryRun will test AI-suggested commands", 40, bold=True), 0, -0.85)),
               up(at_xy(P("before they touch your files", 40, bold=True), 0, -1.6)), rt=0.6)
        c.finish()

class B01_Problem(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("AI assistants suggest terminal commands", 40), 0, 1.5)))
        c.at("coding agents")
        c.play(up(at_xy(P("Coding agents run them", 40), 0, 0.6)))
        c.at("One wrong character")
        c.play(up(at_xy(P("One wrong character can delete files", 40, bold=True), 0, -0.4)))
        c.at("reading a command")
        c.play(FadeIn(chip("THE PROBLEM", 0, 2.35)), up(at_xy(P("Reading a command ≠ knowing what it does", 40), 0, -1.4)))
        c.finish()


class B02_RealReply(Scene):
    def construct(self):
        c = Clock(self); chrome(self, "command quoted exactly · screenshot in evidence/")
        c.play(up(at_xy(P("I asked: delete .log files older than 7 days", 36), 0, 1.45)))
        c.at("It gave me this")
        code = VGroup(at_xy(P('find logs -type f -name "*.log"', 34, font=MONO), 0, 0.34),
                      at_xy(P("-mtime +7 -delete", 34, font=MONO), 0, -0.34))
        c.play(FadeIn(card(10.6, 1.8, 0, 0.0)), up(code), rt=0.55)
        c.at("told me to preview")
        c.play(FadeIn(chip("REAL REPLY · claude.ai · 11 Oct 2026", 0, 2.35)),
               up(at_xy(P("Paraphrased from the reply: preview first, without -delete", 32), 0, -1.55)))
        c.finish()


class B03_Tested(Scene):
    def construct(self):
        c = Clock(self); chrome(self, "evidence/mtime-test.md")
        c.play(up(at_xy(P("Preview, without -delete, on a test folder", 34), 0, 1.5)))
        rows = [("6.5 days old", -0.0), ("7.5 days old", -0.85), ("8.5 days old", -1.7)]
        files = VGroup(*[Rectangle(width=0.42, height=0.55, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=CARD_EDGE,
                                   stroke_width=2).move_to([-4.9, y, 0]) for _, y in rows])
        c.play(FadeIn(chip("TESTED ON MY MAC · 11 Oct 2026", 0, 2.35)), FadeIn(files),
               *[up(at_xy(P(a, 34), -2.6, y)) for a, y in rows], rt=0.55)
        c.at("seven and a half")
        band = Rectangle(width=11.4, height=0.7, fill_color=CHIP, fill_opacity=1, stroke_width=0).move_to([0, -0.85, 0]).set_z_index(-1)
        c.play(FadeIn(band), up(at_xy(P("not matched", 34), 2.0, 0.0)),
               up(at_xy(P("missed: older than 7 days", 34, bold=True), 2.0, -0.85)),
               up(at_xy(P("matched", 34), 2.0, -1.7)), rt=0.55)
        c.finish()

class B04_Copy(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        crate = open_crate(2.6, -4.3, -0.55)
        c.play(up(at_xy(P("It will be a GitHub repository", 42, bold=True), 0, 2.45)), FadeIn(crate),
               up(at_xy(P("your folder", 30), -4.3, -2.25)), rt=0.5)
        c.at("with tests")
        box = DashedVMobject(RoundedRectangle(width=5.0, height=2.6, corner_radius=0.2, stroke_color=INK, stroke_width=3),
                             num_dashes=70).move_to([3.75, -0.6, 0])
        copy = open_crate(2.1, 2.4, -0.6)
        arrow = Arrow([-2.95, -0.6, 0], [1.0, -0.6, 0], buff=0, color=INK, stroke_width=6)
        c.play(up(at_xy(P("+ tests + an evaluation report", 34), 0, 1.75)), GrowArrow(arrow),
               up(at_xy(P("DryRun will make a copy", 24), -0.95, -0.15)),
               Create(box), FadeIn(copy), up(at_xy(P("throwaway copy", 30), 3.75, -2.25)),
               FadeIn(chip("CONSTRUCTED SKETCH", 4.1, 3.08, size=24)), rt=0.5)
        c.at("evaluation report")
        drop = Arrow([3.15, 0.7, 0], [2.8, 0.3, 0], buff=0, color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.4)
        c.play(FadeIn(terminal("find logs … -delete", 4.4, 1.08, w=3.7, h=0.72)), GrowArrow(drop),
               up(at_xy(P("changes happen", 24), 4.8, -0.35)), up(at_xy(P("only here", 24), 4.8, -0.75)),
               up(at_xy(P("Design goal: real files are never touched", 30), 0, -2.95)), rt=0.5)
        c.finish()

class B05_Contract(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("The AI will have to answer in a fixed format", 38), 0, 1.5)))
        c.at("the command")
        c.play(FadeIn(chip("STEP 1 · CONSTRUCTED EXAMPLE", 0, 2.35)), FadeIn(card(11.2, 0.95, 0, 0.35)),
               up(at_xy(P("Command", 30, bold=True), -4.55, 0.35)),
               up(at_xy(P("find logs … -mtime +7 -delete", 30, font=MONO), 0.9, 0.35)), rt=0.5)
        c.at("plus its own prediction")
        c.play(FadeIn(card(11.2, 0.95, 0, -0.85)), up(at_xy(P("Predicted", 30, bold=True), -4.55, -0.85)),
               up(at_xy(P("deletes the 7.5-day and 8.5-day logs", 30), 0.9, -0.85)), rt=0.5)
        c.finish()

class B06_Simulate(Scene):
    def construct(self):
        c = Clock(self); chrome(self, "simulated from my 11 Oct preview test (1 file matched)")
        c.play(up(at_xy(P("Planned: locked container · no network", 36), 0, 1.5)))
        c.at("Then it will compare")
        before = VGroup(at_xy(P("before", 32, bold=True), -3.2, 0.6),
                        *[at_xy(P(f"{a}-day log", 32), -3.2, y) for a, y in (("6.5", -0.15), ("7.5", -0.8), ("8.5", -1.45))])
        after = VGroup(at_xy(P("after", 32, bold=True), 3.2, 0.6),
                       *[at_xy(P(f"{a}-day log", 32), 3.2, y) for a, y in (("6.5", -0.15), ("7.5", -0.8))])
        arrow = Arrow([-1.3, -0.8, 0], [1.3, -0.8, 0], buff=0, color=INK, stroke_width=6)
        c.play(FadeIn(chip("STEP 2 · CONSTRUCTED SIMULATION", 0, 2.35)), up(before), rt=0.5)
        c.at("before and after")
        c.play(GrowArrow(arrow), up(after), rt=0.5)
        c.at("or deleted")
        c.play(up(at_xy(P("Simulated: the 8.5-day log would be deleted", 34, bold=True), 0, -2.35)))
        c.finish()

class B07_Gate(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("Predicted 2 deleted · simulated 1", 36), 0, 1.5)))
        c.at("the task's rules")
        c.play(FadeIn(chip("STEP 3 · CONSTRUCTED EXAMPLE", 0, 2.35)),
               up(at_xy(P("Rule: every .log older than 7 days", 34), 0, 0.75)))
        c.at("Then it will allow")
        gate = prop("permission-gate", 2.3, -4.2, -1.2)
        chips = [chip(s, x, -0.55, size=30) for s, x in (("ALLOW", 0.3), ("WARN", 2.55), ("BLOCK", 4.85))]
        c.play(FadeIn(gate), *[FadeIn(k) for k in chips], rt=0.5)
        c.at("warn, or block")
        mark = Line([2.0, -1.05, 0], [3.1, -1.05, 0], color=INK, stroke_width=6)
        c.play(Create(mark), gate.parts["barrier"].animate.shift(gate.action_vectors["barrier"] * 0.5),
               up(at_xy(P("WARN: 1 matching file not deleted", 32, bold=True), 2.4, -1.7)), rt=0.5)
        c.at("When it can't tell")
        c.play(up(at_xy(P("Can't tell? It will say so.", 30), 2.4, -2.35)))
        c.finish()

class B08_Retry(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("A blocked command's changes will go back to the AI", 36), 0, 1.0)))
        c.at("which will try again")
        loop = Arrow([3.4, -0.1, 0], [-3.4, -0.1, 0], buff=0, color=INK, stroke_width=6)
        c.play(FadeIn(chip("IN A LATER PHASE", 0, 2.35)), GrowArrow(loop),
               up(at_xy(P("It will retry, up to 3 times", 40, bold=True), 0, -1.0)), rt=0.5)
        c.finish()

class B09_Report(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(FadeIn(chip("STEP 4 · REPORT · CONSTRUCTED MOCK-UP", 0, 2.35)), FadeIn(card(11.4, 3.7, 0, -0.05)), rt=0.5)
        rows = [("see the command", "Command", "find logs … -mtime +7 -delete", MONO, 1.15),
                ("its predicted changes", "Predicted", "2 logs deleted", FONT, 0.35),
                ("the real file differences", "Simulated", "1 log deleted", FONT, -0.45)]
        for cue, k, v, font, y in rows:
            c.at(cue)
            c.play(up(at_xy(P(k, 32, bold=True), -4.2, y)), up(at_xy(P(v, 32, font=font), 1.2, y)))
        c.at("The tests and report")
        c.play(Create(Line([-5.3, -0.95, 0], [5.3, -0.95, 0], color=CARD_EDGE, stroke_width=2)),
               up(at_xy(P("Decision: WARN · 1 file missed", 36, bold=True), 0, -1.45)), rt=0.5)
        c.finish()


class B10_Traps(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("I'll build trap folders to catch mistakes", 40, bold=True), 0, 2.1)))
        items = [("names with spaces", "my report.log", MONO, "space in the name", -4.0, 0.75),
                 ("names that look like options", "-rf.log", MONO, "looks like an option", 0.0, 0.75),
                 ("hidden files", ".env.log", MONO, "hidden file", 4.0, 0.75),
                 ("files right at a time limit", "7.5 days old", FONT, "right at the time limit", -3.2, -1.05),
                 ("links that point outside", "link → outside the folder", FONT, "points outside", 2.4, -1.05)]
        for cue, name, font, cap, x, y in items:
            c.at(cue)
            c.play(FadeIn(chip(name, x, y, size=30, font=font, bold=False)), up(at_xy(P(cap, 26), x, y - 0.68)), rt=0.4)
        c.finish()


class B11_Measure(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("Then I'll measure it", 40, bold=True), 0, 2.2)))
        c.at("tasks with known")
        c.play(up(at_xy(P("Tasks with known correct results", 36), 0, 1.4)))
        c.at("across every trap folder")
        c.play(up(at_xy(P("× every trap folder", 36), 0, 0.7)))
        c.at("comparing Claude")
        c.play(FadeIn(chip("Claude", -2.4, -0.1, size=32)), up(at_xy(P("vs", 30), 0, -0.1)),
               FadeIn(chip("free local model", 2.6, -0.1, size=32)), rt=0.45)
        c.at("did too much")
        c.play(up(at_xy(P("Did too much: —", 34), -2.8, -1.2)), up(at_xy(P("Did too little: —", 34), 2.8, -1.2)))
        c.at("or too little")
        c.play(FadeIn(chip("PLANNED · NOT MEASURED YET", 0, -2.15)))
        c.finish()


class B12_Alternatives(Scene):
    def construct(self):
        c = Clock(self); chrome(self, "github.com/binpash/try · arXiv 2306.14898 · arXiv 2502.06858")
        c.play(up(at_xy(P("try: previews a command's file changes", 38), 0, 1.25)))
        c.play(up(at_xy(P("Linux only", 30), 0, 0.55)), rt=0.35)
        c.at("Research benchmarks")
        c.play(Create(rule(-0.1, 2.5)), up(at_xy(P("Research benchmarks: score AI commands offline", 38), 0, -0.85)), rt=0.5)
        c.play(FadeIn(chip("WHAT ALREADY EXISTS", 0, 2.35)), up(at_xy(P("InterCode · NL2SH", 30), 0, -1.55)), rt=0.35)
        c.finish()


class B13_Different(Scene):
    """v4: the whole planned workflow in one picture (Pavithra's reference image, redrawn in the film's
    palette): your folder -> throwaway copy -> compare -> you decide."""
    def construct(self):
        c = Clock(self); chrome(self)
        Y = -0.35
        crate = open_crate(1.8, -5.0, Y)
        box = DashedVMobject(RoundedRectangle(width=2.2, height=2.0, corner_radius=0.18, stroke_color=INK, stroke_width=3),
                             num_dashes=48).move_to([-2.15, Y, 0])
        copy = open_crate(1.3, -2.15, Y)
        a1 = Arrow([-4.05, Y, 0], [-3.35, Y, 0], buff=0, color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.35)
        c.play(up(at_xy(P("DryRun will go one step further", 42, bold=True), 0, 2.4)), FadeIn(chip("PLANNED · CONSTRUCTED SKETCH", 0, 1.6)),
               FadeIn(crate), GrowArrow(a1), Create(box), FadeIn(copy),
               up(at_xy(P("your folder", 26), -5.0, -1.85)), up(at_xy(P("untouched", 24), -5.0, -2.3)),
               up(at_xy(P("throwaway copy", 26), -2.15, -1.85)), up(at_xy(P("command runs here", 24), -2.15, -2.3)), rt=0.6)
        c.at("It will compare")
        a2 = Arrow([-0.95, Y, 0], [-0.3, Y, 0], buff=0, color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.35)
        rows = VGroup(at_xy(P("Change report", 24, bold=True), 1.35, 0.3), at_xy(P("1 log deleted", 24), 1.35, -0.12),
                      Line([0.05, -0.42, 0], [2.65, -0.42, 0], color=INK, stroke_width=2),
                      at_xy(P("vs your request", 24), 1.35, -0.72), at_xy(P("vs AI prediction", 24), 1.35, -1.1))
        c.play(GrowArrow(a2), FadeIn(card(3.2, 2.0, 1.35, Y)), FadeIn(rows),
               up(at_xy(P("compare", 26), 1.35, -1.85)), up(at_xy(P("flags mismatches", 24), 1.35, -2.3)), rt=0.5)
        c.at("and flag mismatches")
        fork = VGroup(*[Arrow([3.05, Y, 0], [3.95, y, 0], buff=0, color=INK, stroke_width=4, max_tip_length_to_length_ratio=0.25)
                        for y in (0.45, Y, -1.15)])
        c.play(*[GrowArrow(a) for a in fork],
               *[FadeIn(chip(t, 4.85, y, size=26)) for t, y in (("ALLOW", 0.45), ("WARN", Y), ("BLOCK", -1.15))],
               up(at_xy(P("you decide", 26), 4.85, -1.85)), up(at_xy(P("before you run it", 24), 4.85, -2.3)), rt=0.5)
        c.finish()

class B14_Skills(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("Course skills it will show", 42, bold=True), 0, 2.25)))
        for cue, s, x, y in (("a prompt contract", "prompt contract", -3.0, 1.15),
                             ("verification that", "verification, not trust", 3.0, 1.15),
                             ("an agent loop", "agent loop", -3.0, 0.0),
                             ("an evaluation you can rerun", "evaluation you can rerun", 3.0, 0.0)):
            c.at(cue)
            c.play(FadeIn(chip(s, x, y, size=34, bold=False)), rt=0.4)
        c.at("A reviewer could")
        c.play(Create(rule(-0.85, 3.0)), up(at_xy(P("Fair conclusion: I can check and measure an AI's work", 34, bold=True), 0, -1.55)), rt=0.5)
        c.at("not that Dry Run")
        c.play(FadeIn(chip("NOT CLAIMED: DryRun makes commands safe", 0, -2.4, size=28)))
        c.finish()


class B15_Scope(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("It will only check files and folders", 38), 0, 1.9)))
        c.at("Network calls")
        c.play(up(at_xy(P("Out: network calls, outside services, databases", 36), 0, 1.0)))
        c.at("The first piece")
        c.play(FadeIn(chip("FIRST PIECE TO RUN", 0, 0.05)),
               up(at_xy(P("one command → one copy → a change list", 36, bold=True), 0, -0.75)), rt=0.5)
        c.at("You'll know it ran")
        c.play(FadeIn(chip("HOW YOU'LL KNOW IT RAN", 0, -1.65)),
               up(at_xy(P("its self-test finds the changes it planted", 34, bold=True), 0, -2.45)), rt=0.5)
        c.finish()


class B16_Intent(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("Hardest part: knowing what you meant", 42, bold=True), 0, 1.3)))
        c.at("I'll start with")
        c.play(up(at_xy(P("I'll start with file tasks that can be checked", 36), 0, 0.0)))
        c.at("report uncertainty")
        c.play(FadeIn(chip("BIGGEST RISK", 0, 2.35)), up(at_xy(P("It will say \u201ccan't tell\u201d instead of guessing", 36), 0, -1.1)))
        c.finish()

class B17_MacLinux(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("My Mac's tools ≠ Linux tools", 40), 0, 1.2)))
        c.play(up(at_xy(P("Same command, different behaviour (e.g. sed -i)", 34), 0, 0.15)), rt=0.45)
        c.at("so the first version")
        c.play(FadeIn(chip("SECOND RISK", 0, 2.35)), up(at_xy(P("Version 1 will target Linux behaviour", 38, bold=True), 0, -1.1)))
        c.finish()

class B18_Why(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("Why DryRun: a stronger portfolio", 42, bold=True), 0, 1.4)))
        c.at("I've built web apps")
        c.play(up(at_xy(P("Built before: web apps", 36), 0, 0.15)), rt=0.45)
        c.at("but nothing")
        c.play(Create(rule(0.75, 2.6)), up(at_xy(P("Missing: a project that checks an AI's work", 36), 0, -0.8)))
        c.finish()


class B19_Learning(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(FadeIn(chip("ALREADY KNOW", -3.2, 1.9)), up(at_xy(P("Python, testing", 36), -3.2, 0.95)),
               up(at_xy(P("internship · PR #33 (32 tests)", 26), -3.2, 0.42)))
        c.at("I've used Docker")
        c.play(up(at_xy(P("Docker", 36), -3.2, -0.25)), up(at_xy(P("Northeastern cloud project", 26), -3.2, -0.78)))
        c.at("Sandboxing")
        c.play(FadeIn(chip("NEW TO ME", 3.2, 1.9)), *[up(at_xy(P(s, 36), 3.2, y)) for s, y in
                                                     (("sandboxing", 0.95), ("file diffing", 0.25), ("evaluation design", -0.45))], rt=0.5)
        c.at("mostly new learning")
        c.play(up(at_xy(P("Mostly new learning", 40, bold=True), 0, -1.7)))
        c.finish()


class B20_Today(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("Today: no DryRun code yet", 42, bold=True), 0, 1.6)))
        c.at("Everything in this film")
        c.play(up(at_xy(P("Everything here is what I will build", 34), 0, 0.7)))
        c.at("in four phases")
        c.play(*[FadeIn(chip(s, x, y, size=30, bold=False)) for s, x, y in
                 (("1 · CLI core", -3.0, -0.45), ("2 · Claude Code hook + retry", 3.0, -0.45),
                  ("3 · evaluation + report", -3.0, -1.45), ("4 · API · dashboard · CI", 3.0, -1.45))], rt=0.45)
        c.finish()


class B21_Close(Scene):
    def construct(self):
        c = Clock(self); chrome(self)
        c.play(up(at_xy(P("DryRun", 72, bold=True), 0, 1.0)))
        c.at("See what")
        c.play(up(at_xy(P("See what an AI's command will do", 38), 0, -0.15)))
        c.at("before it touches")
        c.play(up(at_xy(P("before it touches your files", 38), 0, -0.85)), Create(rule(-1.6, 2.4)),
               up(at_xy(P("Pavithra Prasad · INFO 7375 · Final project pitch", 28), 0, -2.2)), rt=0.45)
        c.finish()
