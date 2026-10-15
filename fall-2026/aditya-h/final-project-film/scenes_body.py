# ═════════════════════════════ AI PRODUCT FAILURE LAB — body scenes (show-tell) ═════════════════════════════
# Written by Claude (Claude Code) for Aditya Hasija, 2026-10-14. build_scenes.sh pastes iso_kit.py and
# iso_originals_25.py above this file to make scenes.py (Gate A copies only scenes.py).
# Cast kept for the whole film: the idea = a kraft crate/parcel, claims = white pages, agents = dark blocks,
# the evaluator = the review desk, the source pack = the evidence binder.
# Every drawing of the unbuilt product carries the corner tag "constructed"; the two baseline beats carry
# "real test · Oct 14" (assignment honesty rule).


def label(s, x, y, size=40):
    return T(s, size=size).move_to([x, y, 0])


def tag(kind="constructed"):
    t = T(kind, size=32)
    t.move_to([6.1 - t.width / 2, -3.15, 0])
    return t


def sheet(x, y, w=2.2, h=2.8, lines=4, gap=0.42):
    """A flat white page with ink outline and grey 'claim' lines; returns (group, line_list)."""
    pg = paper(x, y, w=w, h=h)
    top = y + h / 2 - 0.55
    ls = [Line([x - w / 2 + 0.3, top - i * gap, 0], [x + w / 2 - 0.3 - (0.5 if i == lines - 1 else 0), top - i * gap, 0],
               color=BAR2, stroke_width=6) for i in range(lines)]
    return VGroup(pg, *ls), ls


def small_box(iso, x0, y0, s=0.9):
    return iso.box(x0, y0, 0, s, s, s * 0.8)


_ManimScene = Scene


class Scene(_ManimScene):   # guarded Scene: keeps `class Bxx(Scene)` so run.sh's scene discovery regex still matches
    """Midpoint guard: Gate T and Gate V sample each clip at its midpoint, so no animation may be running then.
    Any play() that would overlap [mid - 0.3 s, mid + 0.3 s] first waits until mid + 0.3 s."""
    MARGIN = 0.3

    def play(self, *anims, **kw):
        target = _TARGET.get(type(self).__name__.split("_")[0], 0)
        rt = kw.get("run_time", 1.0)
        if target and not all(isinstance(x, Wait) for x in anims):
            mid, t0 = target / 2.0, _elapsed(self)
            if t0 < mid + self.MARGIN and t0 + rt > mid - self.MARGIN:
                _ManimScene.wait(self, mid + self.MARGIN - t0)
        return _ManimScene.play(self, *anims, **kw)


class B00_IdeaBox(Scene):
    def construct(self):
        crate = make_original("context-crate", height=3.4, x=-2.2, y=-0.4)
        self.play(FadeIn(crate, shift=DOWN * 1.2), run_time=0.9)
        self.add(tag())
        self.play(FadeIn(label("idea", -2.2, -2.8)), run_time=0.4)
        until(self, "They fail months later")
        self.play(crate.parts["lid"].animate.shift(crate.action_vectors["lid"]), run_time=0.7)
        pages = VGroup(*[sheet(2.4 + i * 1.5, 0.9 - i * 0.35, w=1.6, h=2.1, lines=3, gap=0.38)[0] for i in range(3)])
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.6) for p in pages], lag_ratio=0.3), run_time=1.2)
        until(self, "an assumption nobody checked")
        bad = pages[1][0].sheet
        crack = VMobject(stroke_color=TERRA, stroke_width=8).set_points_as_corners(
            [[3.35, 1.25, 0], [3.75, 0.85, 0], [3.55, 0.55, 0], [4.05, 0.1, 0], [3.85, -0.2, 0]])
        self.play(bad.animate.set_stroke(TERRA, width=7), Create(crack), run_time=0.8)
        self.play(FadeIn(label("assumption", 3.9, -1.9)), run_time=0.4)
        finish(self)


class B01_InOut(Scene):
    def construct(self):
        crate = make_original("context-crate", height=1.7, x=-5.1, y=1.1)
        binder = make_original("evidence-binder", height=1.3, x=-5.1, y=-1.5)
        machine = make_original("server-tower", height=2.6, x=-0.3, y=0.0)
        self.add(machine, tag())
        self.play(FadeIn(crate, shift=RIGHT * 0.6), FadeIn(binder, shift=RIGHT * 0.6), run_time=0.8)
        self.play(FadeIn(label("sources", -5.1, -2.7)), run_time=0.4)
        until(self, "and it will return")
        c2, b2 = crate.copy(), binder.copy()
        self.play(c2.animate.scale(0.35).move_to([-1.0, 0.4, 0]).set_opacity(0),
                  b2.animate.scale(0.35).move_to([-1.0, -0.4, 0]).set_opacity(0), run_time=0.9)
        self.remove(c2, b2)
        light = Dot([0.15, 0.35, 0], radius=0.12, color=TERRA)
        self.play(GrowFromCenter(light), run_time=0.3)
        pages = VGroup(*[sheet(3.3 + i * 1.05, 0.9 - i * 0.55, w=1.5, h=2.0, lines=3, gap=0.36)[0] for i in range(3)])
        until(self, "five failure risks")
        self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.8) for p in pages], lag_ratio=0.45), run_time=1.6)
        self.play(FadeIn(label("pre-mortem", 4.35, -2.6)), run_time=0.4)
        finish(self)


class B02_Repo(Scene):
    def construct(self):
        parcel = make_original("release-parcel", height=3.0, x=-3.2, y=-0.6)
        self.add(tag())
        self.play(FadeIn(parcel, shift=DOWN * 0.8), run_time=0.8)
        self.play(FadeIn(label("GitHub repo", -3.2, -2.9)), run_time=0.4)
        self.play(parcel.parts["lid"].animate.shift(parcel.action_vectors["lid"]), run_time=0.6)
        until(self, "a small web app")
        win = VGroup(Rectangle(width=2.6, height=1.8, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5),
                     Rectangle(width=2.6, height=0.32, fill_color=BAR3, fill_opacity=1, stroke_color=INK, stroke_width=5).shift(UP * 0.74),
                     *[Dot([-1.1 + i * 0.22, 0.74, 0], radius=0.05, color=INK) for i in range(3)],
                     Rectangle(width=1.6, height=0.18, fill_color=BAR2, fill_opacity=1, stroke_width=0).shift(UP * 0.2),
                     Rectangle(width=1.0, height=0.18, fill_color=BAR2, fill_opacity=1, stroke_width=0).shift(DOWN * 0.2 + LEFT * 0.3)
                     ).move_to([1.0, 1.5, 0])
        self.play(FadeIn(win, shift=UP * 0.5), run_time=0.6)
        until(self, "a test set")
        cards = VGroup(*[paper(3.6 + i * 0.5, 1.6 - i * 0.15, w=1.1, h=1.4, tilt=0.18 - i * 0.18) for i in range(3)])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.4) for c in cards], lag_ratio=0.3), run_time=0.8)
        until(self, "a log that scores it")
        log, _ = sheet(2.6, -1.4, w=2.0, h=1.6, lines=3, gap=0.32)
        self.play(FadeIn(log, shift=UP * 0.4), run_time=0.6)
        finish(self)


class B03_Agents(Scene):
    def construct(self):
        iso = Iso(0, 0, 0.9)
        packet = small_box(Iso(-5.6, -0.3, 0.9), 0, 0, 1.0)
        self.add(packet, tag())
        ys = [2.0, 0.0, -2.0]
        blocks = VGroup(*[Iso(-1.6, y - 0.4, 0.75).mcp(0, 0, 0) for y in ys])
        names = ["market", "customer", "risk"]
        wires = VGroup(*[Line([-4.6, 0.1, 0], [-2.2, y, 0], color=DIM, stroke_width=5) for y in ys])
        self.play(LaggedStart(*[Create(w) for w in wires], lag_ratio=0.2), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.3) for b in blocks], lag_ratio=0.2), run_time=0.8)
        self.play(*[FadeIn(label(n, 0.55, y + 0.1, 36)) for n, y in zip(names, ys)], run_time=0.4)
        until(self, "An evaluator will challenge")
        desk = make_original("review-desk", height=2.4, x=4.6, y=-0.3)
        self.play(FadeIn(desk, shift=LEFT * 0.4), run_time=0.6)
        notes = VGroup(*[paper(1.9, y, w=0.7, h=0.9) for y in ys])
        self.play(FadeIn(notes), run_time=0.3)
        self.play(*[n.animate.move_to([4.0 + i * 0.5, 0.6 - i * 0.12, 0]) for i, n in enumerate(notes)], run_time=0.9)
        until(self, "can send one back once")
        self.play(notes[2].animate.move_to([1.9, -2.0, 0]), run_time=0.6)
        self.play(notes[2].animate.move_to([5.0, 0.36, 0]), run_time=0.6)
        until(self, "One retry")
        self.play(FadeIn(label("1 retry", 4.6, -2.4, 36)), run_time=0.4)
        finish(self)


class B04_Baseline(Scene):
    def construct(self):
        left, _ = sheet(-3.2, 0.3, w=3.2, h=3.6, lines=5, gap=0.5)
        right, _ = sheet(3.2, 0.3, w=3.2, h=3.6, lines=5, gap=0.5)
        self.add(tag("real test · Oct 14"))
        self.play(FadeIn(left, shift=UP * 0.4), FadeIn(right, shift=UP * 0.4), run_time=0.8)
        self.play(FadeIn(label("Claude", -3.2, -2.1)), FadeIn(label("ChatGPT", 3.2, -2.1)), run_time=0.4)
        until(self, "with a fake statistic")
        stats = VGroup(T("68%", 52, bold=True).move_to([-3.2, 0.25, 0]), T("68%", 52, bold=True).move_to([3.2, 0.25, 0]))
        self.play(FadeIn(stats, scale=1.2), run_time=0.6)
        until(self, "Both caught")
        rings = VGroup(*[Circle(radius=0.62, color=TERRA, stroke_width=8).move_to(s) for s in stats])
        checks = VGroup(check(-1.9, 0.9, 0.3, TERRA, 9), check(4.5, 0.9, 0.3, TERRA, 9))
        self.play(Create(rings), run_time=0.5)
        self.play(Create(checks), run_time=0.5)
        finish(self)


class B05_Gap(Scene):
    def construct(self):
        left, ll = sheet(-3.2, 0.3, w=3.2, h=3.6, lines=6, gap=0.44)
        right, rl = sheet(3.2, 0.3, w=3.2, h=3.6, lines=6, gap=0.44)
        self.add(left, right, tag("real test · Oct 14"))
        self.play(FadeIn(label("Claude", -3.2, -2.1)), FadeIn(label("ChatGPT", 3.2, -2.1)), run_time=0.5)
        until(self, "cited no sources")
        zero = T("0", 120, bold=True).move_to([-5.9, 0.6, 0])
        self.play(FadeIn(zero, scale=1.3), run_time=0.6)
        until(self, "ChatGPT sourced just two")
        dots = VGroup(*[Dot([1.35, rl[i].get_center()[1], 0], radius=0.11, color=TERRA) for i in (1, 4)])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.4), run_time=0.7)
        until(self, "You can't tell")
        qs = VGroup(*[T("?", 44).move_to([x, 2.55, 0]) for x in (-3.2, 3.2)])
        self.play(FadeIn(qs, shift=DOWN * 0.2), run_time=0.5)
        finish(self)


class B06_PaidReport(Scene):
    def construct(self):
        iso = Iso(-1.6, -2.7, 1.0)
        self.add(tag())
        slabs = VGroup(*[iso.box(0, 0, i * 0.13, 2.4, 3.0, 0.11, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5) for i in range(18)])
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.2) for s in slabs], lag_ratio=0.08), run_time=1.6)
        self.play(FadeIn(label("paid report", 2.2, -2.0)), run_time=0.4)
        until(self, "with hundreds of citations")
        tagshape = VGroup(Polygon([3.0, 1.0, 0], [4.6, 1.0, 0], [4.6, 0.0, 0], [3.0, 0.0, 0], [2.5, 0.5, 0],
                                  fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5),
                          Circle(radius=0.1, color=INK, stroke_width=5).move_to([2.95, 0.5, 0]),
                          T("$", 48).move_to([3.9, 0.5, 0]))
        self.play(FadeIn(tagshape, shift=LEFT * 0.3), run_time=0.6)
        until(self, "I haven't bought one")
        q = T("?", 150, bold=True).move_to([1.6, 2.2, 0])
        self.play(FadeIn(q, scale=0.8), run_time=0.6)
        finish(self)


class B07_Scanner(Scene):
    def construct(self):
        binder = make_original("evidence-binder", height=1.4, x=-5.2, y=-1.0)
        scanner = make_original("checkpoint-scanner", height=3.4, x=-0.8, y=-0.2)
        self.add(scanner, tag())
        self.play(FadeIn(binder, shift=RIGHT * 0.4), run_time=0.6)
        self.play(FadeIn(label("sources", -5.2, -2.2, 36)), run_time=0.3)
        until(self, "Every claim will get a label")
        p1, _ = sheet(3.9, 1.3, w=1.6, h=1.9, lines=3, gap=0.36)
        p2, _ = sheet(3.9, -1.4, w=1.6, h=1.9, lines=3, gap=0.36)
        self.play(scanner.parts["parcel"].animate.shift(scanner.action_vectors["parcel"]), run_time=0.8)
        self.play(FadeIn(p1, shift=RIGHT * 0.4), FadeIn(p2, shift=RIGHT * 0.4), run_time=0.6)
        until(self, "will check each citation")
        link = DashedLine([-4.3, -0.9, 0], [-2.3, -0.3, 0], color=INK, stroke_width=5)
        self.play(Create(link), run_time=0.5)
        t1 = VGroup(pill(5.5, 1.3, 1.7, fill=CARD).set_stroke(INK, 4), T("sourced", 34).move_to([5.5, 1.3, 0]))
        t2 = VGroup(pill(5.5, -1.4, 1.5, fill=BAR3), T("guess", 34).move_to([5.5, -1.4, 0]))
        self.play(FadeIn(t1, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(t2, shift=LEFT * 0.2), run_time=0.4)
        until(self, "including where it loses")
        board = VGroup(*[Rectangle(width=0.45, height=0.28, fill_color=c, fill_opacity=1, stroke_color=INK, stroke_width=3)
                         .move_to([2.0 + i * 0.5, 3.0, 0]) for i, c in enumerate([BAR2, BAR2, CARD, BAR2, CARD])])
        self.play(LaggedStart(*[FadeIn(b) for b in board], lag_ratio=0.2), run_time=0.6)
        finish(self)


class B08_FirstMinute(Scene):
    def construct(self):
        desk = make_original("review-desk", height=2.4, x=0, y=-2.3)
        self.add(desk, tag())
        xs, names = [-4.2, 0.0, 4.2], ["README", "report", "scores"]
        pages = [sheet(x, 1.9, w=2.0, h=2.3, lines=3, gap=0.4)[0] for x in xs]
        cur = cursor(-6.0, 3.3)
        for i, (x, n, ph) in enumerate(zip(xs, names, ["the read", "one real sample report", "the score table"])):
            until(self, ph if ph != "the read" else "they'll read")
            self.play(FadeIn(pages[i], shift=DOWN * 0.5), FadeIn(label(n, x, 0.3, 36)), run_time=0.6)
            if i == 0:
                self.add(cur)
            self.play(cur.animate.move_to([x + 0.6, 1.7, 0]), run_time=0.4)
        finish(self)


class B09_Contract(Scene):
    def construct(self):
        stack = make_original("skill-stack", height=2.0, x=-4.8, y=0.6)
        gate = make_original("permission-gate", height=3.0, x=2.6, y=-0.4)
        self.add(gate, tag())
        self.play(FadeIn(stack, shift=DOWN * 0.3), run_time=0.6)
        self.play(FadeIn(label("contract", -4.8, -0.9)), run_time=0.3)
        outline = DashedVMobject(Square(side_length=1.1, color=INK, stroke_width=5), num_dashes=16).move_to([-0.8, -1.9, 0])
        self.play(Create(outline), FadeIn(label("schema", -0.8, -3.0)), run_time=0.6)
        until(self, "a schema each agent's output")
        parcel = small_box(Iso(-3.6, -2.4, 0.7), 0, 0, 1.0)
        self.play(FadeIn(parcel, shift=RIGHT * 0.3), run_time=0.4)
        self.play(parcel.animate.move_to(outline.get_center()), run_time=0.8)
        until(self, "then measure whether they held")
        self.play(outline.animate.set_color(TERRA), run_time=0.3)
        self.play(gate.parts["barrier"].animate.shift(gate.action_vectors["barrier"]), run_time=0.7)
        self.play(parcel.animate.move_to([3.4, -1.2, 0]), run_time=0.8)
        finish(self)


class B10_Binder(Scene):
    def construct(self):
        binder = make_original("evidence-binder", height=2.6, x=-2.6, y=-0.6)
        self.add(binder, tag())
        self.play(binder.parts["cover"].animate.shift(binder.action_vectors["cover"]), run_time=0.7)
        names = ["logs", "scores", "failures"]
        tabs = []
        for i, n in enumerate(names):
            pg, _ = sheet(1.0 + i * 1.9, 1.2 - i * 0.3, w=1.7, h=2.0, lines=3, gap=0.36)
            tabs.append(VGroup(pg, label(n, 1.0 + i * 1.9, -0.35 - i * 0.3, 36)))
        until(self, "the score table")
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.5) for t in tabs[:2]], lag_ratio=0.4), run_time=0.9)
        until(self, "where it failed")
        self.play(FadeIn(tabs[2], shift=RIGHT * 0.5), tabs[2][0][0].sheet.animate.set_stroke(TERRA, width=7), run_time=0.6)
        finish(self)


class B11_FirstRun(Scene):
    def construct(self):
        belt = make_original("conveyor", height=2.6, x=-2.6, y=-0.6)
        self.add(belt, tag())
        self.play(FadeIn(label("first run", -2.6, -2.6)), run_time=0.4)
        until(self, "on one test idea")
        self.play(belt.parts["parcel"].animate.shift(belt.action_vectors["parcel"]), run_time=1.0)
        until(self, "a run log appears")
        log, _ = sheet(3.6, 0.4, w=2.4, h=2.8, lines=4, gap=0.42)
        self.play(FadeIn(log, shift=DOWN * 0.6), run_time=0.6)
        until(self, "passes the schema check")
        self.play(Create(check(3.6, -0.5, 0.35, TERRA, 10)), run_time=0.5)
        finish(self)


class B12_NoScore(Scene):
    def construct(self):
        gate = make_original("permission-gate", height=3.2, x=1.6, y=-0.4)
        gate.parts["barrier"].shift(gate.action_vectors["barrier"])
        self.add(tag())
        self.play(FadeIn(gate), run_time=0.5)
        card = VGroup(paper(0, 0, w=1.5, h=1.5), T("%", 80, bold=True)).move_to([-5.4, 0.2, 0])
        self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.5)
        self.play(card.animate.move_to([-1.4, 0.2, 0]), run_time=0.9)
        until(self, "turning guesses into a probability")
        self.play(gate.parts["barrier"].animate.shift(-gate.action_vectors["barrier"]), run_time=0.5)
        self.play(FadeIn(label("no score", -1.4, -2.3)), run_time=0.3)
        until(self, "Live web search")
        self.play(card.animate.shift(LEFT * 4.0).set_opacity(0.25), run_time=0.8)
        finish(self)


class B13_RubberStamp(Scene):
    def construct(self):
        st = make_original("approval-stamp", height=3.6, x=-0.6, y=-0.3)
        self.add(st, tag())
        crack = VMobject(stroke_color=TERRA, stroke_width=7).set_points_as_corners(
            [[-1.9, -0.75, 0], [-1.45, -1.0, 0], [-1.65, -1.2, 0], [-1.1, -1.5, 0]])
        self.play(Create(crack), run_time=0.6)
        self.play(FadeIn(label("rubber stamp", 3.9, 1.2)), run_time=0.4)
        until(self, "the same model grading")
        self.play(st.parts["stamp"].animate.shift(st.action_vectors["stamp"]), run_time=0.5)
        self.play(st.parts["stamp"].animate.shift(-st.action_vectors["stamp"]), run_time=0.5)
        ok = check(0.9, -1.2, 0.4, INK, 11)
        self.play(Create(ok), run_time=0.4)
        until(self, "like a price that contradicts")
        self.play(Indicate(crack, color=TERRA, scale_factor=1.15), run_time=0.8)
        finish(self)


class B14_CatchRate(Scene):
    def construct(self):
        bench = make_original("experiment-bench", height=3.0, x=-2.8, y=-0.4)
        self.add(bench, tag())
        self.play(FadeIn(label("catch rate", 3.4, 2.6)), run_time=0.4)
        until(self, "how many planted flaws")
        self.play(bench.parts["sample"].animate.shift(bench.action_vectors["sample"]), run_time=0.7)
        marks = VGroup(*[Line([2.0 + i * 0.4, 1.7, 0], [2.0 + i * 0.4, 0.9, 0], color=INK, stroke_width=9) for i in range(4)])
        marks.add(Line([1.85, 1.0, 0], [3.35, 1.6, 0], color=INK, stroke_width=9))
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.3), run_time=1.2)
        until(self, "into plain code")
        code = Iso(3.0, -2.0, 0.8).mcp(0, 0, 0)
        self.play(FadeIn(code, shift=LEFT * 0.6), run_time=0.6)
        self.play(FadeIn(T("{ }", 44).move_to([4.6, -2.3, 0])), run_time=0.3)
        finish(self)


class B15_Shelves(Scene):
    def construct(self):
        have = make_original("version-shelves", height=3.6, x=-3.3, y=0.0)
        self.play(FadeIn(have, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(label("have", -3.3, -2.5)), run_time=0.3)
        until(self, "New to me")
        slots = VGroup(*[DashedVMobject(Rectangle(width=2.6, height=0.9, color=INK, stroke_width=5), num_dashes=24)
                         .move_to([3.3, 1.3 - i * 1.25, 0]) for i in range(3)])
        self.play(LaggedStart(*[Create(s) for s in slots], lag_ratio=0.35), run_time=1.2)
        self.play(FadeIn(label("new", 3.3, -2.5)), run_time=0.3)
        finish(self)


class B16_Status(Scene):
    def construct(self):
        iso = Iso(-3.6, -1.6, 0.9)
        back, front = iso.open_box(0, 0, 0, 2.4, 2.4, 0.7)
        items = VGroup(iso.page(0.3, 0.3, 0.2, 0.9, 1.0), iso.page(1.2, 1.1, 0.2, 0.9, 1.0),
                       small_box(Iso(-3.6 + 0.6, -1.6 + 1.3, 0.9), 0, 0, 0.6))
        self.play(FadeIn(back), FadeIn(front), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(i, shift=DOWN * 0.3) for i in items], lag_ratio=0.3), run_time=0.8)
        self.play(FadeIn(label("exists", -3.6, -2.7)), run_time=0.3)
        until(self, "Everything else")
        slots = VGroup(*[DashedVMobject(RoundedRectangle(width=1.4, height=1.1, corner_radius=0.1, color=INK, stroke_width=5),
                                        num_dashes=20).move_to([0.2 + (i % 4) * 1.6, 1.0 - (i // 4) * 1.5, 0]) for i in range(8)])
        self.play(LaggedStart(*[Create(s) for s in slots], lag_ratio=0.15), run_time=1.4)
        self.play(FadeIn(label("will build", 2.6, -1.8)), run_time=0.3)
        finish(self)


class BDEFS_Terms(Scene):
    """The two terms, drawn with the film's own cast (replaces the ClaudeDefinitions card, whose fixed
    48px lowercase meanings measure 40px at 4K, one under GATE T's 41px floor)."""
    def construct(self):
        crate = make_original("context-crate", height=2.6, x=-3.6, y=-0.6)
        self.play(FadeIn(crate, shift=DOWN * 0.8), run_time=0.7)
        self.play(FadeIn(label("pre-mortem", -3.6, -2.5, 44)), run_time=0.4)
        crack = VMobject(stroke_color=TERRA, stroke_width=8).set_points_as_corners(
            [[-4.35, -0.55, 0], [-4.0, -0.85, 0], [-4.2, -1.1, 0], [-3.8, -1.45, 0]])
        self.play(Create(crack), run_time=0.5)
        until(self, "and ask why")
        q = T("?", 120, bold=True).move_to([-3.6, 2.2, 0])
        self.play(FadeIn(q, shift=UP * 0.4), run_time=0.5)
        until(self, "And an evaluator")
        desk = make_original("review-desk", height=2.4, x=3.6, y=-0.8)
        self.play(FadeIn(desk, shift=LEFT * 0.4), FadeIn(label("evaluator", 3.6, -2.5, 44)), run_time=0.6)
        until(self, "checks the other")
        pg = paper(3.6, 2.0, w=1.2, h=1.5)
        self.play(FadeIn(pg, shift=DOWN * 0.4), run_time=0.5)
        self.play(Create(check(3.6, 2.0, 0.3, TERRA, 9)), run_time=0.4)
        finish(self)
