
# ═════════════════════════════ DataSentry pitch — scenes (Ethan Gomes, 2026-10-14) ═════════════════════════════
# scenes.py = iso_kit.py + iso_originals_25.py + this file (see build_scenes.sh). Gate A copies only scenes.py.
# One drawing per beat; labels beside objects, ink, >= 32; terracotta only for dots/lights/tape/checks.

MID_MARGIN = 0.26


def G(self, *anims, rt=0.5, **kw):
    """Play, but never across the clip midpoint (GATE T and Gate V sample there)."""
    bid = type(self).__name__.split("_")[0]
    tgt = _TARGET.get(bid, 0)
    if tgt:
        mid, t0 = tgt / 2.0, _elapsed(self)
        if t0 < mid + MID_MARGIN and t0 + rt > mid - MID_MARGIN:
            self.wait(mid + MID_MARGIN - t0)
    self.play(*anims, run_time=rt, **kw)


def L(s, x, y, size=36, bold=False):
    return T(s, size, INK, bold).move_to([x, y, 0])


def parcel(iso, x0, y0, z0=0.0, w=1.0, d=1.0, h=0.8, flaw=False):
    """A kraft parcel (a batch of rows). `flaw` adds one terracotta dot on its top face (a planted defect)."""
    g = VGroup(iso.box(x0, y0, z0, w, d, h))
    if flaw:
        g.add(Dot(iso.p(x0 + w * 0.5, y0 + d * 0.5, z0 + h), radius=0.09, color=TERRA))
    return g


def table_card(x, y, w=5.4, h=3.6, rows=6):
    """A flat data table: kraft-shadowed white card, a grey header band of 5 column blocks, grey row bars."""
    card = paper(x, y, w=w, h=h)
    top = y + h / 2
    cols = VGroup(*[RoundedRectangle(width=(w - 0.8) / 5 - 0.12, height=0.34, corner_radius=0.08,
                                     fill_color=BAR1, fill_opacity=1, stroke_width=0)
                    .move_to([x - w / 2 + 0.4 + (i + 0.5) * (w - 0.8) / 5, top - 0.45, 0]) for i in range(5)])
    bars = VGroup(*[RoundedRectangle(width=w - 0.8, height=0.24, corner_radius=0.06, fill_color=BAR1,
                                     fill_opacity=1, stroke_width=0)
                    .move_to([x, top - 1.0 - i * (h - 1.35) / max(1, rows - 1), 0]) for i in range(rows)])
    return card, cols, bars


def tray(ox, oy, s=1.0, w=2.6, d=2.6, h=0.45):
    """A shallow kraft tray on a DIM grey plinth (a pale kraft object alone fails Gate V contrast)."""
    iso = Iso(ox, oy, s)
    back, front = iso.open_box(0, 0, 0, w, d, h)
    plinth = iso.box(-0.15, -0.15, -0.28, w + 0.3, d + 0.3, 0.28, BAR1, "#6F737A", "#5F636A")
    plinth.set_z_index(-1)
    back.add_to_back(plinth)
    return iso, back, front


def block_in(iso, gx, gy, w=0.8, d=0.8, h=0.6, dark=False):
    b = iso.box(gx, gy, 0.02, w, d, h, *((DARK_TOP, DARK_L, DARK_R) if dark else (BOX_TOP, BOX_L, BOX_R)))
    b.set_z_index(1.0 + (6 - gx - gy) * 0.05)
    return b


def tall_scribbles(page, n=3, inset=0.25, gap=0.5, amp=0.11):
    """scribbles_on() with taller strokes: the kit's 0.07 amplitude measures ~40 px at 4K, under GATE T's 41 px floor."""
    w = page.w - 2 * inset
    x0, y0 = page.cx - w / 2, page.cy + page.h / 2 - inset - 0.15
    return VGroup(*[scribble(x0, y0 - i * gap, w * (0.62 if i == n - 1 else 1.0), amp=amp) for i in range(n)])


# A variant of the approved scanner prop for this film (Ethan, 2026-10-14): the near (left) leg's top cap is dropped,
# so the top bar sits over the leg instead of the leg's cap showing on top of the bar. The toolkit prop is unchanged.
import copy as _copy
_SC = _copy.deepcopy(_ST_ORIGINALS_25["checkpoint-scanner"])
_SC["parts"]["near-post"] = _SC["parts"]["near-post"][:2]      # keep the two side faces; drop the top face
_ST_ORIGINALS_25["checkpoint-scanner-under"] = _SC



def scanner(height, x, y):
    """The film's scanner rig with explicit layering (Ethan, 2026-10-14): the moving block passes BEHIND the top bar,
    the near leg stays in front, the far leg stays behind the block. Arch parts 0-2 are the far leg; 3-6 the bar + light."""
    rig = make_original("checkpoint-scanner-under", height=height, x=x, y=y)
    arch = list(rig.parts["arch"])
    for m in arch[:3]:
        m.set_z_index(0)
    for m in arch[3:]:
        m.set_z_index(2)
    rig.parts["parcel"].set_z_index(1)
    rig.parts["near-post"].set_z_index(3)
    return rig


class BIDEA_Title(Scene):
    """Title card (Ethan's request, 2026-10-14): the project name, a drawn rule with one terracotta dot, one line on what it is."""
    def construct(self):
        name = L("DataSentry", 0, 0.85, 120, bold=True)
        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.8)
        until(self, "created by")
        rule = Line([-4.2, -0.35, 0], [3.9, -0.35, 0], color=BAR1, stroke_width=5)
        G(self, Create(rule), rt=0.8)
        dot = Dot([4.25, -0.35, 0], radius=0.13, color=TERRA)
        G(self, GrowFromCenter(dot), rt=0.3)
        until(self, "The project is called")
        line = L("Scoring AI-written data checks with planted defects", 0, -1.25, 44)
        G(self, FadeIn(line, shift=UP * 0.1), rt=0.6)
        finish(self)


class B00_Scanner(Scene):
    """Q1: the hero object. The scanner lands, the name lands, the table (parcel) rides under the arch."""
    def construct(self):
        rig = scanner(4.4, -1.6, -0.1)
        vec = rig.action_vectors["parcel"]
        rig.parts["parcel"].shift(vec)                     # parcel waits outside, front-left
        self.play(FadeIn(rig, shift=DOWN * 0.25), run_time=0.8)
        until(self, "Data Sentry")
        name = L("DataSentry", 3.9, 0.9, 60, bold=True)
        G(self, FadeIn(name), rt=0.4)
        until(self, "writes data checks")
        tag = L("a table", 1.3, -2.45, 36)
        G(self, FadeIn(tag), rt=0.3)
        G(self, rig.parts["parcel"].animate.shift(-vec), rt=1.2, rate_func=smooth)
        until(self, "planting defects")
        dot = Dot(np.array(rig.parts["parcel"].get_center()) + np.array([0, 0.25, 0]), radius=0.1, color=TERRA).set_z_index(1.5)
        G(self, GrowFromCenter(dot), rt=0.4)
        finish(self)


class B01_Repo(Scene):
    """Q1: the artifact. The repo crate opens; the three parts rise beside it, each labelled once."""
    def construct(self):
        crate = make_original("context-crate", height=3.6, x=-3.6, y=-0.3)
        self.play(FadeIn(crate, shift=DOWN * 0.25), run_time=0.7)
        until(self, "GitHub repo")
        G(self, crate.parts["lid"].animate.shift(crate.action_vectors["lid"] * 0.9), rt=0.8)
        iso = Iso(0.0, 0.0, 1.0)
        part1 = Iso(0.55, 1.35, 0.85).page(0, 0, 0, w=1.2, d=1.2)
        part2 = Iso(0.55, -0.55, 0.85).mcp(0, 0, 0, w=1.2, d=1.2, h=0.6)
        part3 = make_original("evidence-binder", height=1.25, x=0.95, y=-2.2)
        l1, l2, l3 = L("check writer", 3.9, 1.85), L("defect planter", 3.9, 0.0), L("scorecard", 3.9, -2.1)
        until(self, "a check writer")
        G(self, FadeIn(part1, shift=UP * 0.3), FadeIn(l1), rt=0.5)
        until(self, "a defect planter")
        G(self, FadeIn(part2, shift=UP * 0.3), FadeIn(l2), rt=0.5)
        until(self, "and a scorecard")
        G(self, FadeIn(part3, shift=UP * 0.3), FadeIn(l3), rt=0.5)
        finish(self)


class B02_Table(Scene):
    """The data: a public taxi-trip table; rows stack, then the five columns block in as they are named."""
    def construct(self):
        card, cols, bars = table_card(-1.3, -0.3, w=7.2, h=4.6, rows=7)
        self.play(FadeIn(card, shift=DOWN * 0.2), run_time=0.6)
        until(self, "New York City")
        l1 = L("NYC taxi trips", -1.3, 2.75, 40)
        G(self, FadeIn(l1), rt=0.4)
        until(self, "ten thousand rows")
        G(self, LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.12), rt=1.2)
        l2 = VGroup(T("~10,000", 48, bold=True), T("rows", 36)).arrange(DOWN, buff=0.12).move_to([4.6, -0.3, 0])
        G(self, FadeIn(l2), rt=0.4)
        for phrase, c in zip(["Pick-up time", "drop-off time", "passengers", "distance", "and fare"], cols):
            until(self, phrase)
            G(self, GrowFromCenter(c), rt=0.3)
        finish(self)


class B03_Writer(Scene):
    """Claude Code writes pandera checks from column names only; the defect list stays locked away."""
    def construct(self):
        ws = make_original("agent-workstation", height=3.4, x=-3.9, y=0.0)
        self.play(FadeIn(ws, shift=DOWN * 0.25), run_time=0.7)
        l1 = L("Claude Code", -3.9, -2.4)
        self.play(FadeIn(l1), run_time=0.3)
        until(self, "write checks")
        pages = VGroup(*[Iso(0.2, -0.9 + i * 0.32, 0.9).page(0, 0, 0, w=1.3, d=1.5) for i in range(3)])
        G(self, LaggedStart(*[FadeIn(pg, shift=DOWN * 0.4) for pg in pages], lag_ratio=0.3), rt=0.9)
        l2 = L("pandera checks", 0.25, -2.4)
        G(self, FadeIn(l2), rt=0.3)
        until(self, "never see")
        vault = make_original("secure-vault", height=2.6, x=4.4, y=0.3)
        l3 = L("defect list", 4.4, -1.75)
        G(self, FadeIn(vault, shift=DOWN * 0.25), FadeIn(l3), rt=0.6)
        finish(self)


class B04_Planter(Scene):
    """A script copies the clean table and breaks the copy five ways; one terracotta mark per defect named."""
    def construct(self):
        c1, h1, b1 = table_card(-3.3, -0.2, w=4.8, h=3.8, rows=5)
        self.play(FadeIn(VGroup(c1, h1, b1), shift=DOWN * 0.2), run_time=0.6)
        l1 = L("clean", -3.3, 2.35)
        self.play(FadeIn(l1), run_time=0.3)
        until(self, "copy the clean sample")
        c2, h2, b2 = table_card(3.1, -0.2, w=4.8, h=3.8, rows=5)
        G(self, FadeIn(VGroup(c2, h2, b2), shift=RIGHT * 0.6), rt=0.7)
        l2 = L("broken", 3.1, 2.35)
        G(self, FadeIn(l2), rt=0.3)
        marks = VGroup(*[Dot(np.array(b.get_right()) + np.array([-0.3, 0, 0]), radius=0.11, color=TERRA) for b in b2])
        for phrase, m in zip(["duplicates", "missing values", "impossible numbers", "a drop-off", "wrong type"], marks):
            until(self, phrase)
            G(self, GrowFromCenter(m), rt=0.3)
        five = L("5", 3.1, -2.75, 56, bold=True)
        G(self, FadeIn(five), rt=0.3)
        finish(self)


class B05_TwoRuns(Scene):
    """Every check runs twice: the clean parcel passes the scanner, the broken one is stopped under the arch."""
    def construct(self):
        rig = scanner(4.4, -1.0, -0.1)
        vec = np.array(rig.action_vectors["parcel"])
        rig.parts["parcel"].shift(vec)
        self.play(FadeIn(rig, shift=DOWN * 0.2), run_time=0.6)
        until(self, "On the clean copy")
        G(self, rig.parts["parcel"].animate.shift(-2 * vec), rt=1.4, rate_func=linear)
        G(self, FadeOut(rig.parts["parcel"], shift=-vec * 0.6), rt=0.4)
        ok = check(3.0, 1.6, s=0.3)
        lp = L("pass", 3.9, 1.55)
        G(self, Create(ok), FadeIn(lp), rt=0.4)
        until(self, "On the broken copy")
        bad = rig.parts["parcel"].copy().shift(2 * vec)
        bad.set_z_index(1)
        flaw = Dot(np.array(bad.get_center()) + np.array([0, 0.3, 0]), radius=0.1, color=TERRA).set_z_index(1.5)
        G(self, FadeIn(VGroup(bad, flaw)), rt=0.3)
        G(self, VGroup(bad, flaw).animate.shift(-vec), rt=0.9, rate_func=smooth)
        lf = L("fail", 3.9, -1.0)
        stop = Dot([3.0, -1.0, 0], radius=0.13, color=TERRA)
        G(self, GrowFromCenter(stop), FadeIn(lf), rt=0.4)
        finish(self)


class B06_Dbt(Scene):
    """Alternative one: dbt. Its four built-in tests drop into the left tray as they are named."""
    def construct(self):
        isoA, backA, frontA = tray(-3.3, -1.1)
        isoB, backB, frontB = tray(3.3, -1.1)
        self.play(FadeIn(VGroup(backA, frontA, backB, frontB), shift=DOWN * 0.2), run_time=0.6)
        until(self, "First, D B T")
        la = L("dbt", -3.3, -1.95, 40)
        G(self, FadeIn(la), rt=0.3)
        spots = [(0.35, 0.35), (1.45, 0.35), (0.35, 1.45), (1.45, 1.45)]
        for phrase, (gx, gy) in zip(["unique", "not null", "accepted values", "relationships"], spots):
            until(self, phrase)
            G(self, FadeIn(block_in(isoA, gx, gy), shift=DOWN * 0.5), rt=0.35, rate_func=ease_in)
        finish(self)


def _dbt_tray():
    isoA, backA, frontA = tray(-3.3, -1.1)
    blocks = VGroup(*[block_in(isoA, gx, gy) for gx, gy in [(0.35, 0.35), (1.45, 0.35), (0.35, 1.45), (1.45, 1.45)]])
    return VGroup(backA, blocks, frontA), L("dbt", -3.3, -1.95, 40)


class B07_Gx(Scene):
    """Alternative two: GX Cloud's ExpectAI. Suggested check pages fill the right tray; one gets approved."""
    def construct(self):
        left, la = _dbt_tray()
        isoB, backB, frontB = tray(3.3, -1.1)
        self.add(left, la, backB, frontB)
        self.wait(0.3)
        until(self, "G X Cloud")
        lb = L("GX Cloud", 3.3, -1.95, 40)
        G(self, FadeIn(lb), rt=0.3)
        until(self, "suggests checks")
        pages = VGroup(*[Iso(3.3, -1.1, 1.0).page(0.6, 0.55, 0.05 + i * 0.12, w=1.4, d=1.5) for i in range(3)])
        for pg in pages:
            pg.set_z_index(1.2)
        G(self, LaggedStart(*[FadeIn(pg, shift=DOWN * 0.5) for pg in pages], lag_ratio=0.35), rt=1.0)
        until(self, "review and approve")
        ok = check(5.15, 1.55, s=0.28)
        G(self, Create(ok), rt=0.4)
        until(self, "already exist")
        le = L("ExpectAI", 3.3, 2.55, 36)
        G(self, FadeIn(le), rt=0.3)
        finish(self)


class B08_Gap(Scene):
    """The gap: a broken parcel slides past both trays, unmeasured; a question mark lands beside it."""
    def construct(self):
        left, la = _dbt_tray()
        isoB, backB, frontB = tray(3.3, -1.1)
        pages = VGroup(*[Iso(3.3, -1.1, 1.0).page(0.6, 0.55, 0.05 + i * 0.12, w=1.4, d=1.5) for i in range(3)])
        for pg in pages:
            pg.set_z_index(1.2)
        lb = L("GX Cloud", 3.3, -1.95, 40)
        self.add(left, la, backB, pages, frontB, lb)
        self.wait(0.3)
        until(self, "a way to measure")
        box = parcel(Iso(-5.6, -3.2, 0.5), 0, 0, 0, flaw=True)
        G(self, FadeIn(box), rt=0.3)
        G(self, box.animate.shift(RIGHT * 10.6), rt=2.0, rate_func=smooth)
        until(self, "which bad rows")
        q = L("?", 5.85, -2.6, 72, bold=True)
        G(self, FadeIn(q, shift=UP * 0.2), rt=0.4)
        finish(self)


class B09_FirstMinute(Scene):
    """Who opens it: one command in a terminal, then a short table of defect types (constructed mock-up)."""
    def construct(self):
        win = RoundedRectangle(width=8.0, height=4.8, corner_radius=0.18, fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=4).move_to([-1.5, -0.1, 0])
        shadow = win.copy().set_fill(BOX_L).set_stroke(width=0).shift([0.14, -0.14, 0])
        bar = RoundedRectangle(width=7.6, height=0.42, corner_radius=0.1, fill_color=BAR1, fill_opacity=1,
                               stroke_width=0).move_to([-1.5, 1.95, 0])
        self.play(FadeIn(VGroup(shadow, win, bar), shift=DOWN * 0.2), run_time=0.6)
        lh = L("hiring manager", 4.5, 2.6)
        self.play(FadeIn(lh), run_time=0.3)
        until(self, "one command")
        cmd = RoundedRectangle(width=4.2, height=0.3, corner_radius=0.08, fill_color=INK, fill_opacity=1,
                               stroke_width=0).move_to([-3.2, 1.25, 0])
        lc = L("one command", 4.5, 1.25)
        G(self, GrowFromEdge(cmd, LEFT), FadeIn(lc), rt=0.6)
        until(self, "see each defect")
        rows = VGroup(*[RoundedRectangle(width=4.6, height=0.22, corner_radius=0.06, fill_color=BAR2, fill_opacity=1,
                                         stroke_width=0).move_to([-2.4, 0.45 - i * 0.55, 0]) for i in range(5)])
        rings = VGroup(*[Circle(radius=0.16, stroke_color=INK, stroke_width=4).move_to([1.1, 0.45 - i * 0.55, 0])
                         for i in range(5)])
        G(self, LaggedStart(*[GrowFromEdge(r, LEFT) for r in rows], lag_ratio=0.15), rt=0.8)
        G(self, LaggedStart(*[Create(c) for c in rings], lag_ratio=0.15), rt=0.6)
        lk = L("constructed", 4.5, -2.0, 34)
        G(self, FadeIn(lk), rt=0.3)
        finish(self)


class B10_Proves(Scene):
    """What it proves: the evidence binder opens; four record sheets land in a row, numbered 1 to 4."""
    def construct(self):
        binder = make_original("evidence-binder", height=2.4, x=-4.4, y=0.0)
        self.play(FadeIn(binder, shift=DOWN * 0.2), run_time=0.6)
        G(self, binder.parts["cover"].animate.shift(binder.action_vectors["cover"] * 0.8), rt=0.6)
        xs = [-1.2, 0.75, 2.7, 4.65]
        sheets = [paper(x, 0.35, w=1.5, h=2.0) for x in xs]
        nums = [L(str(i + 1), x, -1.15, 44, bold=True) for i, x in enumerate(xs)]
        for phrase, sh, n in zip(["a prompt contract", "an agent loop", "verification", "evaluation"], sheets, nums):
            until(self, phrase)
            G(self, FadeIn(sh, shift=DOWN * 0.3), FadeIn(n), rt=0.4)
            G(self, Create(tall_scribbles(sh, n=3, gap=0.5)), rt=0.4)
        finish(self)


class B10A_Conclude(Scene):
    """What a reviewer could fairly conclude: tested, not trusted. Then the planned evidence lands on the review desk."""
    def construct(self):
        desk = make_original("review-desk", height=3.2, x=-2.6, y=0.1)
        vec = np.array(desk.action_vectors["evidence"])
        desk.parts["evidence"].shift(vec * 1.6)               # the evidence waits off the desk, to the right
        desk.parts["evidence"].set_opacity(0)
        self.play(FadeIn(desk, shift=DOWN * 0.2), run_time=0.6)
        lr = L("a reviewer", -2.6, -2.35)
        self.play(FadeIn(lr), run_time=0.3)
        until(self, "test an AI")
        lt = L("tested, not trusted", 4.1, 0.55)
        ok = check(1.78, 0.54, s=0.32)                     # beside the label, on its line (Ethan, 2026-10-14)
        G(self, Create(ok), FadeIn(lt), rt=0.5)
        until(self, "The evidence")
        sheets = [make_original("evidence-binder", height=0.9, x=1.6, y=-1.6),
                  paper(3.3, -1.55, w=0.9, h=1.15), Iso(4.75, -2.05, 0.6).page(0, 0, 0, w=1.2, d=1.2)]
        for sh, phrase in zip(sheets, ["the scorecard", "the log", "the prompts"]):
            until(self, phrase)
            G(self, FadeIn(sh, shift=DOWN * 0.3), rt=0.35)
        desk.parts["evidence"].set_opacity(1)
        G(self, desk.parts["evidence"].animate.shift(-vec * 1.6), rt=0.7, rate_func=smooth)
        lp = L("planned evidence", 3.3, -2.75, 34)
        G(self, FadeIn(lp), rt=0.3)
        finish(self)


class B11_Scope(Scene):
    """Scope: three things drop into the 'in' box; Airflow stays outside; the first run prints one line."""
    def construct(self):
        iso, back, front = tray(-2.6, -1.4, s=1.0, w=2.8, d=2.8, h=0.9)
        self.play(FadeIn(VGroup(back, front), shift=DOWN * 0.2), run_time=0.5)
        li = L("in scope", -2.6, 2.6)
        self.play(FadeIn(li), run_time=0.3)
        until(self, "one table")
        pg = Iso(-2.6, -1.4, 1.0).page(1.4, 1.3, 0.02, w=1.2, d=1.2).set_z_index(1.0)
        G(self, FadeIn(pg, shift=DOWN * 0.6), rt=0.35, rate_func=ease_in)
        until(self, "five defect types")
        pk = parcel(iso, 1.5, 0.3, 0.02, w=0.9, d=0.9, h=0.6, flaw=True).set_z_index(1.1)
        G(self, FadeIn(pk, shift=DOWN * 0.6), rt=0.35, rate_func=ease_in)
        until(self, "one scorecard")
        bk = block_in(iso, 0.3, 1.5, w=0.9, d=0.9, h=0.4, dark=True)
        G(self, FadeIn(bk, shift=DOWN * 0.6), rt=0.35, rate_func=ease_in)
        until(self, "orchestration")
        stack, lights = Iso(3.6, -0.6, 0.9).server(0, 0, 0, w=1.3, d=1.3, slab=0.42, n=3)
        la = L("Airflow: out", 3.6, -1.9)
        G(self, FadeIn(VGroup(stack, lights), shift=DOWN * 0.2), FadeIn(la), rt=0.5)
        until(self, "First to run")
        slip = paper(-2.6, -2.75, w=3.4, h=0.7)
        line = scribble(-3.9, -2.75, 2.0, amp=0.05)
        G(self, FadeIn(slip, shift=DOWN * 0.15), rt=0.35)
        G(self, Create(line), rt=0.5)
        ok = check(-0.45, -2.7, s=0.2)
        lf = L("first run", 1.4, -2.75)
        G(self, Create(ok), FadeIn(lf), rt=0.4)
        finish(self)


class B12_Loose(Scene):
    """The risk: with the barrier up (a loose check), a broken parcel rides straight through; then it comes down."""
    def construct(self):
        gate = make_original("permission-gate", height=3.8, x=-0.6, y=0.1)
        up = np.array(gate.action_vectors["barrier"])
        gate.parts["barrier"].shift(up)
        gate.parts["posts"].set_z_index(2); gate.parts["barrier"].set_z_index(2.2)
        self.play(FadeIn(gate, shift=DOWN * 0.2), run_time=0.6)
        lt = L("too loose", 4.3, 2.2)
        self.play(FadeIn(lt), run_time=0.3)
        centre = np.array(gate.parts["base"].get_center(), dtype=float)
        along = np.array([-0.866, 0.5, 0.0])          # iso y axis: through the opening, front to back

        def crate_at(pt):
            c = parcel(Iso(float(pt[0]), float(pt[1]) - 0.54, 0.6), 0, 0, 0, flaw=True)
            c.set_z_index(1)
            return c
        until(self, "passes everything")
        bad = crate_at(centre - along * 1.9)
        G(self, FadeIn(bad), rt=0.3)
        G(self, bad.animate.shift(along * 2.9), rt=1.6, rate_func=linear)
        G(self, FadeOut(bad), rt=0.4)
        until(self, "So the clean")
        G(self, gate.parts["barrier"].animate.shift(-up), rt=0.6)
        bad2 = crate_at(centre - along * 2.7)
        bad2.set_z_index(3)
        G(self, FadeIn(bad2), rt=0.3)
        G(self, bad2.animate.shift(along * 1.6), rt=0.8, rate_func=smooth)
        lb = L("both copies", 4.3, -1.6)
        G(self, FadeIn(lb), rt=0.3)
        finish(self)


class B13_Why(Scene):
    """Why this project: the skills I'm working on fill a tray, and an arrow carries them to the hiring desk (B10A's desk)."""
    def construct(self):
        isoA, backA, frontA = tray(-3.6, -1.1)
        self.play(FadeIn(VGroup(backA, frontA), shift=DOWN * 0.2), run_time=0.5)
        lw = L("working on", -3.6, -1.95)
        self.play(FadeIn(lw), run_time=0.3)
        until(self, "land a data job")
        desk = make_original("review-desk", height=2.8, x=3.5, y=0.45)
        r1, r2 = L("Data Engineer", 3.5, -1.55, 36), L("Data Analyst", 3.5, -2.2, 36)
        G(self, FadeIn(desk, shift=DOWN * 0.2), FadeIn(r1), FadeIn(r2), rt=0.6)
        spots = [(0.35, 0.35, False), (1.45, 0.35, False), (0.35, 1.45, False), (1.45, 1.45, True)]
        for phrase, (gx, gy, dark) in zip(["Python", "pandas", "pandera", "Claude Code"], spots):
            until(self, phrase)
            G(self, FadeIn(block_in(isoA, gx, gy, dark=dark), shift=DOWN * 0.5), rt=0.35, rate_func=ease_in)
        until(self, "fixes its own")
        arrow = Line([-1.1, 0.35, 0], [1.4, 0.35, 0], color=INK, stroke_width=7)
        tip = Dot([1.5, 0.35, 0], radius=0.12, color=TERRA)
        G(self, Create(arrow), rt=0.5)
        G(self, GrowFromCenter(tip), rt=0.25)
        finish(self)


class B14_Exists(Scene):
    """Exists today vs will exist: three real pages land on the left; three empty slots stay on the right."""
    def construct(self):
        divider = Line([0, 2.2, 0], [0, -2.4, 0], color=INK, stroke_width=4)
        date = L("2026-10-14", 0, 2.8, 36)
        self.play(Create(divider), FadeIn(date), run_time=0.5)
        le = L("exists", -3.1, -2.75, 40)
        lw = L("will exist", 3.1, -2.75, 40)
        xs = [-4.9, -3.1, -1.3]
        for phrase, x in zip(["this pitch", "a written brief", "my notes"], xs):
            until(self, phrase)
            pg = paper(x, -0.2, w=1.5, h=2.1)
            G(self, FadeIn(pg, shift=DOWN * 0.3), rt=0.35)
            G(self, Create(tall_scribbles(pg, n=3, gap=0.55)), rt=0.4)
            if x == xs[0]:
                G(self, FadeIn(le), rt=0.3)
        for phrase, x in zip(["the code", "the defect planter", "any score"], [1.3, 3.1, 4.9]):
            until(self, phrase)
            slot = RoundedRectangle(width=1.5, height=2.1, corner_radius=0.08, fill_color=BAR1, fill_opacity=1,
                                    stroke_color=INK, stroke_width=4).move_to([x, -0.2, 0])
            G(self, FadeIn(slot), rt=0.35)
            if x == 1.3:
                G(self, FadeIn(lw), rt=0.3)
        finish(self)


class BEND_Close(Scene):
    """Close: the scanner returns; the title and Ethan's name land beside it."""
    def construct(self):
        rig = scanner(3.8, -3.2, -0.1)
        vec = rig.action_vectors["parcel"]
        rig.parts["parcel"].shift(vec)
        self.play(FadeIn(rig, shift=DOWN * 0.2), run_time=0.4)
        title = L("DataSentry", 2.4, 0.5, 64, bold=True)
        name = L("Ethan Gomes", 2.4, -0.55, 40)
        self.play(FadeIn(title), run_time=0.35)
        self.play(FadeIn(name), run_time=0.35)
        G(self, rig.parts["parcel"].animate.shift(-vec), rt=0.8, rate_func=smooth)
        light = Dot(np.array(rig.parts["parcel"].get_center()) + np.array([0, 0.22, 0]), radius=0.09, color=TERRA).set_z_index(1.5)
        G(self, GrowFromCenter(light), rt=0.3)
        finish(self)
