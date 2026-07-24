# -----------------------------------------------------------------------------
# MOCK DATA ONLY
# This entire file is fictional proof-of-concept content for the
# National Masonry Society "Code Provenance Tracker" demo.
# No real code text, real proposals, or real people are represented.
# -----------------------------------------------------------------------------

from datetime import date

# -----------------------------------------------------------------------------
# PROPOSALS
# status: "accepted" | "under_review" | "declined"
# -----------------------------------------------------------------------------

PROPOSALS = {

    "P-2022-014": {
        "id": "P-2022-014",
        "status": "accepted",
        "title": "Minimum grout compressive strength increase for reinforced CMU shear walls",
        "code_section": "3.2.1",
        "chapter": "Chapter 3 — Mortar & Grout",
        "submitted_by": "T. Ferraro, Structural Engineer, Ferraro & Boyd Associates",
        "date_submitted": "2022-03-11",
        "date_decided": "2022-09-08",
        "committee": "Materials & Testing Subcommittee",
        "vote": "9–1 in favor",
        "summary": "Raises the minimum specified compressive strength for grout used in reinforced CMU shear walls from 2,000 psi to 2,500 psi at 28 days, aligning with updated regional seismic loading studies.",
        "reasoning": "Field failure data from three 2019–2021 seismic retrofit projects showed grout consolidation voids correlating with lower observed strengths near the 2,000 psi floor. The committee found that a 2,500 psi minimum provides an adequate margin without materially increasing material cost (est. 3–5% per CY), and matches the direction already taken by two neighboring state amendments.",
        "old_text": "Grout used in reinforced masonry shear walls shall have a minimum specified compressive strength of 2,000 psi at 28 days.",
        "new_text": "Grout used in reinforced masonry shear walls shall have a minimum specified compressive strength of 2,500 psi at 28 days, tested in accordance with ASTM C1019.",
        "correspondence": [
            {"date": "2022-03-11", "author": "T. Ferraro", "role": "Proposer",
             "message": "Submitting proposal based on grout core sampling from the Millbrook Ave retrofit (2021). Voids observed in 6 of 24 cores taken at the legacy 2,000 psi mix design."},
            {"date": "2022-04-02", "author": "Materials & Testing Subcommittee",
             "role": "Committee", "message": "Assigned to subcommittee for review. Requesting supporting lab data and cost impact analysis before first hearing."},
            {"date": "2022-05-19", "author": "T. Ferraro", "role": "Proposer",
             "message": "Attached lab reports (Meridian Testing Labs, Reports #4471–#4478) and a cost memo estimating 3-5% increase in grout material cost per cubic yard."},
            {"date": "2022-06-14", "author": "D. Whitfield", "role": "Committee Reviewer",
             "message": "Public comment period opened. One objection received from Coastal Masonry Suppliers Assoc. citing regional aggregate availability at higher strength mixes; response requested."},
            {"date": "2022-07-01", "author": "T. Ferraro", "role": "Proposer",
             "message": "Response filed: 2,500 psi mixes are achievable with standard Type S grout aggregates readily available in all NMS regions per attached supplier survey."},
            {"date": "2022-09-08", "author": "Materials & Testing Subcommittee",
             "role": "Committee", "message": "APPROVED 9-1. Effective in next code cycle publication. Dissent (1) cited desire for phased implementation; noted for record."},
        ],
    },

    "P-2022-031": {
        "id": "P-2022-031",
        "status": "accepted",
        "title": "Required vertical reinforcement spacing reduction in high-seismic wall segments",
        "code_section": "4.1.5",
        "chapter": "Chapter 4 — Reinforcement",
        "submitted_by": "N. Okafor, P.E., City of Rivergate Building Dept.",
        "date_submitted": "2022-06-02",
        "date_decided": "2023-01-17",
        "committee": "Seismic Design Task Group",
        "vote": "7–2 in favor",
        "summary": "Reduces maximum vertical reinforcement spacing in Seismic Design Category D/E/F wall segments from 48 inches to 32 inches on center.",
        "reasoning": "Post-event reconnaissance from the 2021 Cascade Ridge earthquake sequence identified diagonal shear cracking concentrated in wall segments using the prior 48-inch maximum spacing. Task group modeling (ASCE 7-22 aligned) showed a 32-inch spacing reduces peak crack width by an estimated 35% under design-level shaking without a significant labor cost increase, since most contractors in high-seismic regions already exceed the minimum in practice.",
        "old_text": "In Seismic Design Categories D, E, and F, vertical reinforcement in masonry shear wall segments shall be spaced not more than 48 inches on center.",
        "new_text": "In Seismic Design Categories D, E, and F, vertical reinforcement in masonry shear wall segments shall be spaced not more than 32 inches on center, except where an engineering analysis per Section 7.4 demonstrates equivalent performance.",
        "correspondence": [
            {"date": "2022-06-02", "author": "N. Okafor", "role": "Proposer",
             "message": "Submitting following joint post-earthquake reconnaissance report with the Structural Engineers Coalition. Photos and crack mapping attached (Appendix C)."},
            {"date": "2022-07-20", "author": "Seismic Design Task Group", "role": "Committee",
             "message": "Full task group review scheduled. Requesting independent modeling to corroborate field observations before advancing."},
            {"date": "2022-10-05", "author": "R. Solis", "role": "Independent Reviewer (Kessler Structural)",
             "message": "Modeling results attached. Confirms meaningful reduction in peak crack width at 32\" spacing under MCE-level demand; recommend allowing an engineered exception path for unusual geometries."},
            {"date": "2022-11-12", "author": "Masonry Contractors Guild", "role": "Public Comment",
             "message": "Supportive, with note that an engineered-exception clause (as modeled by Kessler) would prevent unnecessary rework on non-standard wall configurations."},
            {"date": "2023-01-17", "author": "Seismic Design Task Group", "role": "Committee",
             "message": "APPROVED 7-2 with the engineered-exception clause included per public comment. Dissent (2) preferred a 36\" threshold instead of 32\"; noted for record."},
        ],
    },

    "P-2023-002": {
        "id": "P-2023-002",
        "status": "accepted",
        "title": "Weep hole spacing clarification for cavity wall drainage systems",
        "code_section": "5.3.4",
        "chapter": "Chapter 5 — Wall Construction",
        "submitted_by": "L. Padgett, Building Envelope Consultants Inc.",
        "date_submitted": "2023-02-08",
        "date_decided": "2023-06-22",
        "committee": "Wall Systems Subcommittee",
        "vote": "Unanimous",
        "summary": "Clarifies that weep hole maximum spacing of 24 inches on center applies measured along the wall base, and adds a requirement for weeps directly above all flashing terminations and lintels.",
        "reasoning": "Ambiguity in the prior text led to inconsistent interpretation of whether the 24-inch spacing was measured horizontally or along a sloped condition, causing field disputes flagged by inspectors in four separate jurisdictions. The added requirement for weeps above flashing terminations closes a known drainage gap that has been an informal best practice for a decade but was never codified.",
        "old_text": "Weep holes shall be provided at a maximum spacing of 24 inches on center in the head joints of the first course of masonry above flashing.",
        "new_text": "Weep holes shall be provided at a maximum spacing of 24 inches on center, measured horizontally along the base of the wall, in the head joints of the first course of masonry above flashing. Additionally, a weep hole shall be provided directly above each flashing termination and above each lintel, regardless of the regular spacing pattern.",
        "correspondence": [
            {"date": "2023-02-08", "author": "L. Padgett", "role": "Proposer",
             "message": "Four jurisdictions (list attached) have issued conflicting field interpretations on this section over the past two years. Requesting clarifying language plus a codified requirement over lintels."},
            {"date": "2023-03-01", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "Non-controversial clarification; fast-tracked to single hearing per Rule 4.2."},
            {"date": "2023-06-22", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "APPROVED unanimously. No dissent recorded."},
        ],
    },

    "P-2023-019": {
        "id": "P-2023-019",
        "status": "accepted",
        "title": "Prescriptive anchor spacing for veneer ties in high-wind regions",
        "code_section": "5.6.2",
        "chapter": "Chapter 5 — Wall Construction",
        "submitted_by": "H. Nakamura, Coastal Structures Group",
        "date_submitted": "2023-04-14",
        "date_decided": "2024-02-09",
        "committee": "Wall Systems Subcommittee",
        "vote": "8–1 in favor",
        "summary": "Introduces tighter prescriptive veneer tie spacing (16 in. o.c. vertical / 24 in. o.c. horizontal) for structures in Wind Exposure Category D, replacing the prior blanket table that did not differentiate by exposure category.",
        "reasoning": "Insurance-industry storm damage data (2018-2022) submitted alongside the proposal showed veneer tie pull-out was disproportionately concentrated in Exposure D construction using the old blanket spacing table. The tighter spacing adds an estimated 12% more ties per elevation in the affected exposure category only, which the committee found justified by the loss data.",
        "old_text": "Veneer anchors shall be spaced not more than 24 inches on center vertically and 32 inches on center horizontally, regardless of wind exposure category.",
        "new_text": "Veneer anchors shall be spaced not more than 24 inches on center vertically and 32 inches on center horizontally, except that in Wind Exposure Category D, spacing shall not exceed 16 inches on center vertically and 24 inches on center horizontally.",
        "correspondence": [
            {"date": "2023-04-14", "author": "H. Nakamura", "role": "Proposer",
             "message": "Submitting with aggregated storm claims data from three regional insurers showing a pattern in Exposure D veneer failures tied to anchor spacing."},
            {"date": "2023-05-30", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "Requested underlying claims dataset be anonymized and independently summarized before entering into public record."},
            {"date": "2023-09-11", "author": "H. Nakamura", "role": "Proposer",
             "message": "Anonymized summary attached, prepared by Gulf Coast Risk Analytics."},
            {"date": "2023-11-20", "author": "Precast & Veneer Suppliers Assoc.", "role": "Public Comment",
             "message": "Generally supportive; requested a 2-year phase-in for supply chain adjustment on tie hardware. Not incorporated into final text but noted for future transition guidance."},
            {"date": "2024-02-09", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "APPROVED 8-1. Dissent (1) felt the phase-in request should have been codified rather than left as guidance."},
        ],
    },

    "P-2024-006": {
        "id": "P-2024-006",
        "status": "accepted",
        "title": "Bond beam requirement at diaphragm connections in Seismic Design Category D+",
        "code_section": "7.2.3",
        "chapter": "Chapter 7 — Seismic Design Provisions",
        "submitted_by": "M. Alvarez, Alvarez Structural Group",
        "date_submitted": "2023-08-19",
        "date_decided": "2024-05-03",
        "committee": "Seismic Design Task Group",
        "vote": "6–3 in favor",
        "summary": "Requires a continuous reinforced bond beam at every roof and floor diaphragm connection for structures in Seismic Design Category D and above, closing a load-path gap identified in peer-reviewed failure studies.",
        "reasoning": "A load path discontinuity at diaphragm-to-wall connections was identified as a contributing factor in two independent university-led failure studies following the 2021 and 2022 seismic events referenced elsewhere in this code cycle's proposals. The task group weighed cost impact carefully given the 6-3 vote margin; ultimately the majority found the life-safety benefit outweighed the added reinforcement cost, but limited the requirement to SDC D and above rather than applying it universally, addressing the dissent's cost concerns for lower-seismic regions.",
        "old_text": "Bond beams are recommended, but not required, at roof and floor diaphragm connections.",
        "new_text": "In Seismic Design Category D and above, a continuous reinforced bond beam shall be provided at every roof and floor diaphragm connection, detailed in accordance with Section 7.4.",
        "correspondence": [
            {"date": "2023-08-19", "author": "M. Alvarez", "role": "Proposer",
             "message": "Submitting with citations to two peer-reviewed post-earthquake failure studies (Univ. of Cascadia Structural Lab, 2022; attached as Exhibits A & B)."},
            {"date": "2023-10-02", "author": "Seismic Design Task Group", "role": "Committee",
             "message": "Extended review requested given cost implications; referred to joint session with Cost Impact Review Panel."},
            {"date": "2024-01-15", "author": "Cost Impact Review Panel", "role": "Committee",
             "message": "Estimated statewide cost impact memo delivered: ~1.8% increase in average wall system cost for SDC D+ structures only. No impact for lower SDC regions under proposed scope-limited text."},
            {"date": "2024-03-04", "author": "Regional Builders Coalition", "role": "Public Comment",
             "message": "Opposed universal application; supportive of the scope-limited (SDC D+) version now on the table."},
            {"date": "2024-05-03", "author": "Seismic Design Task Group", "role": "Committee",
             "message": "APPROVED 6-3 as scope-limited to SDC D and above. Dissent (3) preferred deferring for one more cycle pending further cost data."},
        ],
    },

    # -------------------------------------------------------------------
    # UNDER REVIEW
    # -------------------------------------------------------------------

    "P-2025-004": {
        "id": "P-2025-004",
        "status": "under_review",
        "title": "Increase minimum net area compressive strength (f'm) for load-bearing CMU above 4 stories",
        "code_section": "3.2.1",
        "chapter": "Chapter 3 — Mortar & Grout",
        "submitted_by": "K. Bergstrom, Bergstrom Tall Wall Consulting",
        "date_submitted": "2025-01-22",
        "committee": "Materials & Testing Subcommittee",
        "stage": "Public comment period (closes 2026-09-15)",
        "summary": "Proposes raising the minimum net area masonry compressive strength (f'm) from 1,500 psi to 2,000 psi specifically for load-bearing CMU walls in structures exceeding four stories, citing increased demand from mid-rise mass masonry projects.",
        "reasoning_so_far": "Proposer argues current minimum was calibrated for low-rise construction and doesn't reflect the axial loads now common in the growing mid-rise CMU sector. Committee has requested independent cost-benefit analysis before proceeding to a vote; that analysis is due before the next scheduled hearing.",
        "old_text": "Load-bearing masonry walls shall have a minimum specified net area compressive strength (f'm) of 1,500 psi.",
        "proposed_text": "Load-bearing masonry walls in structures of five stories or more shall have a minimum specified net area compressive strength (f'm) of 2,000 psi. Structures of four stories or fewer shall continue to use the 1,500 psi minimum specified elsewhere in this section.",
        "correspondence": [
            {"date": "2025-01-22", "author": "K. Bergstrom", "role": "Proposer",
             "message": "Submitting in response to growing mid-rise mass masonry demand in the Pacific Northwest and Mountain West markets. Attaching three case studies of recent 5-7 story CMU load-bearing projects."},
            {"date": "2025-03-10", "author": "Materials & Testing Subcommittee", "role": "Committee",
             "message": "Accepted for review. Requesting independent cost-benefit analysis and comparison against IBC high-rise masonry provisions before scheduling a vote."},
            {"date": "2025-06-01", "author": "K. Bergstrom", "role": "Proposer",
             "message": "Interim update: cost-benefit consultant (Iron Peak Engineering) engaged, report expected Q3 2026."},
            {"date": "2026-05-14", "author": "National CMU Producers Council", "role": "Public Comment",
             "message": "Supportive in principle; requests the story-count threshold be reconsidered as a height-in-feet threshold instead, to avoid penalizing tall-story commercial designs under 5 stories."},
        ],
    },

    "P-2025-011": {
        "id": "P-2025-011",
        "status": "under_review",
        "title": "Mandatory horizontal joint reinforcement in all veneer wythes regardless of exposure",
        "code_section": "5.6.2",
        "chapter": "Chapter 5 — Wall Construction",
        "submitted_by": "J. Marsh, Marsh & Cole Building Consultants",
        "date_submitted": "2025-05-02",
        "committee": "Wall Systems Subcommittee",
        "stage": "First committee hearing scheduled 2026-08-20",
        "summary": "Would require horizontal joint reinforcement at 16 inches on center in all masonry veneer wythes, removing the current exemption for low-exposure (Exposure B) construction.",
        "reasoning_so_far": "Proposer cites isolated cracking incidents in Exposure B veneer, but the subcommittee has flagged that the supporting incident count (4 cases) may be too small a sample to justify removing the exposure-based exemption; additional data has been requested before the first hearing.",
        "old_text": "Horizontal joint reinforcement shall be provided at 16 inches on center in masonry veneer wythes, except in Wind Exposure Category B, where reinforcement is not required.",
        "proposed_text": "Horizontal joint reinforcement shall be provided at 16 inches on center in all masonry veneer wythes regardless of wind exposure category.",
        "correspondence": [
            {"date": "2025-05-02", "author": "J. Marsh", "role": "Proposer",
             "message": "Submitting based on four documented cracking incidents in nominally low-exposure veneer, suggesting the Exposure B exemption may be miscalibrated."},
            {"date": "2025-07-18", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "Sample size of 4 incidents flagged as thin for a blanket rule change. Requesting a broader incident survey across member jurisdictions before first hearing."},
            {"date": "2026-02-27", "author": "J. Marsh", "role": "Proposer",
             "message": "Broader survey submitted: 11 additional incidents identified across 6 jurisdictions via member survey. Full dataset attached."},
        ],
    },

    "P-2025-017": {
        "id": "P-2025-017",
        "status": "under_review",
        "title": "Alternative grouting method for partially grouted shear walls using self-consolidating grout",
        "code_section": "3.4.1",
        "chapter": "Chapter 3 — Mortar & Grout",
        "submitted_by": "S. Whitcombe, Whitcombe Materials Science Lab",
        "date_submitted": "2025-09-10",
        "committee": "Materials & Testing Subcommittee",
        "stage": "Awaiting proposer response to committee questions",
        "summary": "Would add self-consolidating grout (SCG) as an approved alternative placement method for partially grouted shear walls, with its own slump-flow and consolidation verification protocol.",
        "reasoning_so_far": "SCG is already permitted in several adjacent jurisdictions' amendments, and the proposer argues it reduces void rates versus conventional grout in narrow cell configurations. Committee has asked for third-party durability data beyond the proposer's own lab, since Whitcombe Materials Science Lab also manufactures an SCG product line, to address a flagged conflict-of-interest concern.",
        "old_text": "(No existing provision; SCG is not currently an approved placement method under this section.)",
        "proposed_text": "Self-consolidating grout (SCG) meeting the slump-flow and visual stability index criteria of Appendix G may be used as an alternative to conventional grout in partially grouted shear walls, subject to third-party verification testing per Section 3.4.5.",
        "correspondence": [
            {"date": "2025-09-10", "author": "S. Whitcombe", "role": "Proposer",
             "message": "Submitting with lab void-rate comparison data (Whitcombe Materials Science Lab internal report #22-SCG-04)."},
            {"date": "2025-10-28", "author": "Materials & Testing Subcommittee", "role": "Committee",
             "message": "Noted that proposer's lab also manufactures an SCG product. Requesting independent third-party durability data to avoid conflict-of-interest concerns before scheduling a hearing."},
            {"date": "2026-04-06", "author": "S. Whitcombe", "role": "Proposer",
             "message": "Independent testing engaged at Halbrook Independent Labs; results expected Q4 2026."},
        ],
    },

    # -------------------------------------------------------------------
    # DECLINED  (repository of past rejections, for future reference)
    # -------------------------------------------------------------------

    "P-2021-009": {
        "id": "P-2021-009",
        "status": "declined",
        "title": "Elimination of weep hole requirement for rainscreen-backed veneer systems",
        "code_section": "5.3.4",
        "chapter": "Chapter 5 — Wall Construction",
        "submitted_by": "G. Chu, Chu Facade Consultants",
        "date_submitted": "2021-02-14",
        "date_decided": "2021-08-03",
        "committee": "Wall Systems Subcommittee",
        "vote": "1–8 against",
        "summary": "Proposed eliminating the weep hole requirement entirely for veneer systems backed by a certified rainscreen drainage cavity, arguing the drainage cavity alone was sufficient.",
        "reason_declined": "The committee found that rainscreen cavities manage bulk water but do not eliminate the need for a discharge path at the base of the wall; without weeps, incidental moisture can accumulate at the cavity base regardless of the rainscreen. Testing data submitted by the proposer covered short-duration wind-driven rain events only and did not address long-duration or freeze-thaw conditions common in northern NMS member regions. The committee declined but encouraged resubmission if longer-duration and freeze-thaw performance data becomes available.",
        "resubmission_note": "If revisited: request freeze-thaw and long-duration wind-driven rain test data before re-opening this topic. See correspondence for the specific test protocol gap identified in 2021.",
        "correspondence": [
            {"date": "2021-02-14", "author": "G. Chu", "role": "Proposer",
             "message": "Submitting based on short-duration wind tunnel testing showing rainscreen cavities alone managed bulk water intrusion in tested conditions."},
            {"date": "2021-04-22", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "Noted that submitted testing did not address freeze-thaw or long-duration events. Requested supplemental data."},
            {"date": "2021-06-30", "author": "G. Chu", "role": "Proposer",
             "message": "No additional data available at this time; requesting the committee proceed to a vote on existing record."},
            {"date": "2021-08-03", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "DECLINED 1-8. Existing record insufficient to demonstrate performance across the full range of climates in NMS member regions. Filed for potential resubmission with expanded data."},
        ],
    },

    "P-2022-045": {
        "id": "P-2022-045",
        "status": "declined",
        "title": "Reduction of minimum mortar joint thickness from 3/8 in. to 1/4 in. for architectural thin veneer",
        "code_section": "5.6.1",
        "chapter": "Chapter 5 — Wall Construction",
        "submitted_by": "P. Ionescu, Ionescu Design Build",
        "date_submitted": "2022-07-01",
        "date_decided": "2023-01-17",
        "committee": "Wall Systems Subcommittee",
        "vote": "2–7 against",
        "summary": "Proposed reducing minimum mortar joint thickness for architectural thin veneer from 3/8 inch to 1/4 inch to accommodate a narrower joint aesthetic increasingly requested by architects.",
        "reason_declined": "Committee found insufficient bond-strength testing at the proposed 1/4-inch thickness; existing ASTM C270 bond strength data referenced by the proposer was generated at 3/8-inch and 1/2-inch joint thicknesses only, and the committee was unwilling to extrapolate bond performance to a thinner joint without direct testing. Aesthetic rationale alone was not considered sufficient basis absent performance data.",
        "resubmission_note": "If revisited: direct ASTM C270 bond-strength testing at the proposed 1/4-inch thickness is required, not extrapolation from thicker-joint data.",
        "correspondence": [
            {"date": "2022-07-01", "author": "P. Ionescu", "role": "Proposer",
             "message": "Submitting on behalf of several architecture firms requesting a narrower joint reveal for contemporary facade designs."},
            {"date": "2022-09-14", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "Requested direct bond-strength testing at the proposed thickness; noted existing referenced data was generated at thicker joint dimensions."},
            {"date": "2022-11-02", "author": "P. Ionescu", "role": "Proposer",
             "message": "No new testing available before this cycle's deadline; requesting vote on existing aesthetic and precedent-based rationale."},
            {"date": "2023-01-17", "author": "Wall Systems Subcommittee", "role": "Committee",
             "message": "DECLINED 2-7. Aesthetic rationale alone insufficient without direct bond-strength data at proposed thickness. Filed for resubmission if testing becomes available."},
        ],
    },

    "P-2023-028": {
        "id": "P-2023-028",
        "status": "declined",
        "title": "Removal of engineered exception path for reduced vertical reinforcement spacing",
        "code_section": "4.1.5",
        "chapter": "Chapter 4 — Reinforcement",
        "submitted_by": "Regional Builders Coalition",
        "date_submitted": "2023-03-15",
        "date_decided": "2023-09-12",
        "committee": "Seismic Design Task Group",
        "vote": "3–6 against",
        "summary": "Sought to remove the engineered-exception clause added under P-2022-031, arguing it created inconsistent enforcement across jurisdictions with varying plan-review rigor.",
        "reason_declined": "The task group acknowledged enforcement variability as a legitimate concern but declined to remove the exception outright, since doing so would eliminate a pathway explicitly requested by the same commenting parties during the P-2022-031 hearing. Instead, the committee suggested a future proposal focused on standardizing the engineering documentation required to invoke the exception, rather than eliminating it.",
        "resubmission_note": "If revisited: reframe as a documentation/standardization proposal rather than an outright removal — see linked P-2022-031 correspondence for the original intent of the exception clause.",
        "correspondence": [
            {"date": "2023-03-15", "author": "Regional Builders Coalition", "role": "Proposer",
             "message": "Requesting removal of the engineered-exception clause in Section 4.1.5, citing inconsistent plan-review acceptance across jurisdictions."},
            {"date": "2023-05-20", "author": "Seismic Design Task Group", "role": "Committee",
             "message": "Notes that this same coalition supported inclusion of the exception clause during the P-2022-031 hearing. Requesting clarification on what changed."},
            {"date": "2023-07-11", "author": "Regional Builders Coalition", "role": "Proposer",
             "message": "Clarifying that the concern is inconsistent documentation standards at plan review, not the existence of the exception itself."},
            {"date": "2023-09-12", "author": "Seismic Design Task Group", "role": "Committee",
             "message": "DECLINED 3-6. Suggest resubmission as a documentation-standardization proposal rather than removal of the exception. Related to P-2022-031."},
        ],
    },

    "P-2024-033": {
        "id": "P-2024-033",
        "status": "declined",
        "title": "Blanket exemption from bond beam requirement for single-story accessory structures",
        "code_section": "7.2.3",
        "chapter": "Chapter 7 — Seismic Design Provisions",
        "submitted_by": "Regional Builders Coalition",
        "date_submitted": "2024-06-10",
        "date_decided": "2025-02-04",
        "committee": "Seismic Design Task Group",
        "vote": "4–5 against",
        "summary": "Sought a blanket exemption from the new bond beam requirement (P-2024-006) for single-story accessory structures under 600 sq ft, regardless of seismic design category.",
        "reason_declined": "The task group had just adopted the bond beam requirement (P-2024-006) specifically scoped to SDC D and above after extensive cost-impact review, and found that a size-based blanket exemption would reopen the same load-path gap the prior proposal was written to close, for a category of structures (accessory buildings) that can still pose life-safety risk in high seismic zones. Committee noted this proposal was filed only weeks after P-2024-006's adoption and encouraged the proposer to bring size-based data, not just structure-type, to any future resubmission.",
        "resubmission_note": "If revisited: bring engineering data specific to load-path risk in small structures, not just a size/use-based exemption argument. This is a near-immediate follow-on to P-2024-006 and reviewers should read that record first.",
        "correspondence": [
            {"date": "2024-06-10", "author": "Regional Builders Coalition", "role": "Proposer",
             "message": "Requesting exemption for small accessory structures (sheds, small storage buildings) under 600 sq ft from the newly adopted bond beam requirement."},
            {"date": "2024-08-22", "author": "Seismic Design Task Group", "role": "Committee",
             "message": "Notes this proposal follows closely on the heels of P-2024-006's adoption. Requesting engineering rationale specific to reduced risk in small structures, not just size/use classification."},
            {"date": "2024-11-05", "author": "Regional Builders Coalition", "role": "Proposer",
             "message": "No additional engineering data submitted; requesting vote based on cost-burden rationale for small structure owners."},
            {"date": "2025-02-04", "author": "Seismic Design Task Group", "role": "Committee",
             "message": "DECLINED 4-5. Cost-burden argument alone insufficient given the life-safety basis of the parent requirement (P-2024-006). Filed for resubmission with structure-specific risk data if pursued again."},
        ],
    },
}

# -----------------------------------------------------------------------------
# CODE TEXT
# Highlighted spans are marked inline with a simple token syntax that the
# app parses at render time:
#   [[ACC:P-XXXX-XXX]] ... [[/ACC]]   -> light-green, links to an accepted proposal
#   [[REV:P-XXXX-XXX]] ... [[/REV]]   -> light-yellow, links to an under-review proposal
# -----------------------------------------------------------------------------

CODE_CHAPTERS = [
    {
        "id": "ch1",
        "number": "Chapter 1",
        "title": "General Provisions & Scope",
        "sections": [
            {
                "id": "1.1",
                "heading": "1.1 — Scope",
                "body": (
                    "This standard governs the design, materials, and construction of masonry "
                    "structures and structural elements regulated under the jurisdiction of the "
                    "National Masonry Society. It applies to unreinforced and reinforced masonry, "
                    "veneer systems, and glass unit masonry, whether load-bearing or non-load-bearing."
                ),
            },
            {
                "id": "1.2",
                "heading": "1.2 — Referenced Standards",
                "body": (
                    "Where this standard references an ASTM, ACI, or TMS standard by designation "
                    "without a publication year, the most recently adopted edition at the time of "
                    "permit application shall govern. A complete list of referenced standards is "
                    "maintained in Appendix A."
                ),
            },
            {
                "id": "1.6",
                "heading": "1.6 — Testing Agencies",
                "body": (
                    "All testing agencies performing verification testing required by this standard "
                    "shall be accredited under a nationally recognized accreditation program and "
                    "approved by the authority having jurisdiction prior to performing work."
                ),
            },
        ],
    },
    {
        "id": "ch2",
        "number": "Chapter 2",
        "title": "Definitions & Materials",
        "sections": [
            {
                "id": "2.1",
                "heading": "2.1 — Definitions",
                "body": (
                    "Terms used in this standard shall have the meanings given in Appendix B unless "
                    "the context clearly indicates otherwise. Where a term is not defined in this "
                    "standard, its ordinary construction-industry meaning shall apply."
                ),
            },
            {
                "id": "2.2",
                "heading": "2.2 — Masonry Units",
                "body": (
                    "Concrete masonry units shall conform to ASTM C90. Clay and shale brick shall "
                    "conform to ASTM C216 or ASTM C652 as applicable. Units showing chips, cracks, "
                    "or other defects exceeding the limits of the referenced standard shall be rejected."
                ),
            },
            {
                "id": "2.4",
                "heading": "2.4 — Corrosion Protection of Metal Accessories",
                "body": (
                    "Joint reinforcement, anchors, ties, and other metal accessories embedded in or "
                    "attached to masonry shall be protected against corrosion in accordance with "
                    "Table 2.4-A, based on their exposure classification. Stainless steel accessories "
                    "meeting ASTM A580 are exempt from additional coating requirements."
                ),
            },
        ],
    },
    {
        "id": "ch3",
        "number": "Chapter 3",
        "title": "Mortar & Grout",
        "sections": [
            {
                "id": "3.1",
                "heading": "3.1 — Mortar Types and Proportions",
                "body": (
                    "Mortar shall be Type M, S, N, or O as defined in ASTM C270, proportioned by "
                    "either the proportion specification or the property specification of that "
                    "standard, but not both within a single project without written approval."
                ),
            },
            {
                "id": "3.2.1",
                "heading": "3.2.1 — Grout Compressive Strength",
                "body": (
                    "[[ACC:P-2022-014]]Grout used in reinforced masonry shear walls shall have a "
                    "minimum specified compressive strength of 2,500 psi at 28 days, tested in "
                    "accordance with ASTM C1019.[[/ACC]] Sampling frequency shall follow Table 3.2.1-A "
                    "for all structures exceeding two stories in height. "
                    "[[REV:P-2025-004]]Load-bearing masonry walls shall have a minimum specified net "
                    "area compressive strength (f'm) of 1,500 psi.[[/REV]] Verification testing shall "
                    "be performed by an independent testing agency approved under Section 1.6."
                ),
            },
            {
                "id": "3.3",
                "heading": "3.3 — Mixing",
                "body": (
                    "Mortar and grout shall be machine mixed for a minimum of 3 minutes with the "
                    "maximum quantity of water consistent with workability. Mortar that has begun "
                    "to stiffen may be retempered within two hours of initial mixing; grout shall not "
                    "be retempered."
                ),
            },
            {
                "id": "3.4.1",
                "heading": "3.4.1 — Grout Placement Methods",
                "body": (
                    "Conventional grout shall be placed in lifts not exceeding 5 feet unless "
                    "high-lift grouting provisions of Section 3.4.3 are followed. "
                    "[[REV:P-2025-017]](No existing provision currently governs the use of "
                    "self-consolidating grout as an alternative placement method for partially "
                    "grouted shear walls; a proposal to add such a provision is presently under "
                    "committee review.)[[/REV]] All grout placement shall be inspected in accordance "
                    "with the special inspection requirements of Chapter 1."
                ),
            },
            {
                "id": "3.5",
                "heading": "3.5 — Cold Weather Construction",
                "body": (
                    "When the ambient temperature falls below 40°F, masonry materials shall be heated "
                    "and completed masonry protected in accordance with Table 3.5-A. Frozen or "
                    "ice-coated masonry units shall not be laid."
                ),
            },
        ],
    },
    {
        "id": "ch4",
        "number": "Chapter 4",
        "title": "Reinforcement",
        "sections": [
            {
                "id": "4.1.1",
                "heading": "4.1.1 — General",
                "body": (
                    "Reinforcing bars shall conform to ASTM A615, A706, or A996. Bars shall be free "
                    "of loose rust, mill scale, oil, or other coatings that would reduce bond with "
                    "grout at the time of placement."
                ),
            },
            {
                "id": "4.1.5",
                "heading": "4.1.5 — Vertical Reinforcement Spacing",
                "body": (
                    "[[ACC:P-2022-031]]In Seismic Design Categories D, E, and F, vertical "
                    "reinforcement in masonry shear wall segments shall be spaced not more than "
                    "32 inches on center, except where an engineering analysis per Section 7.4 "
                    "demonstrates equivalent performance.[[/ACC]] In Seismic Design Categories A, B, "
                    "and C, vertical reinforcement spacing shall not exceed 48 inches on center. "
                    "Reinforcement shall be secured against displacement prior to grouting."
                ),
            },
            {
                "id": "4.2",
                "heading": "4.2 — Placement Tolerances",
                "body": (
                    "Reinforcement shall be placed within a tolerance of plus or minus 1/2 inch for "
                    "members 8 inches or less in depth, and plus or minus 1 inch for members greater "
                    "than 8 inches in depth, measured from the specified position."
                ),
            },
            {
                "id": "4.3",
                "heading": "4.3 — Splices",
                "body": (
                    "Lap splices shall develop the full tensile strength of the reinforcement unless "
                    "a mechanical or welded splice conforming to Section 4.3.2 is used. Minimum lap "
                    "length shall be as specified in Table 4.3-A."
                ),
            },
        ],
    },
    {
        "id": "ch5",
        "number": "Chapter 5",
        "title": "Wall Construction",
        "sections": [
            {
                "id": "5.1",
                "heading": "5.1 — General",
                "body": (
                    "Masonry walls shall be laid plumb, true to line, and with courses level, unless "
                    "otherwise indicated on the approved construction documents. Bond pattern shall be "
                    "as specified; where not specified, running bond shall be used."
                ),
            },
            {
                "id": "5.2",
                "heading": "5.2 — Bracing During Construction",
                "body": (
                    "Masonry walls under construction shall be adequately braced to resist wind and "
                    "construction loads until permanent lateral support is in place. Temporary bracing "
                    "shall remain until the structure is capable of resisting design loads."
                ),
            },
            {
                "id": "5.3.4",
                "heading": "5.3.4 — Weep Holes and Drainage",
                "body": (
                    "[[ACC:P-2023-002]]Weep holes shall be provided at a maximum spacing of 24 inches "
                    "on center, measured horizontally along the base of the wall, in the head joints "
                    "of the first course of masonry above flashing. Additionally, a weep hole shall be "
                    "provided directly above each flashing termination and above each lintel, "
                    "regardless of the regular spacing pattern.[[/ACC]] Weep holes shall be kept free of "
                    "mortar droppings and other obstructions during construction."
                ),
            },
            {
                "id": "5.4",
                "heading": "5.4 — Control and Expansion Joints",
                "body": (
                    "Control joints in concrete masonry and expansion joints in clay masonry shall be "
                    "provided at intervals not exceeding those given in Table 5.4-A, and at all "
                    "locations of abrupt change in wall height, thickness, or foundation condition."
                ),
            },
            {
                "id": "5.5",
                "heading": "5.5 — Lintels",
                "body": (
                    "Lintels over openings shall be designed for the loads imposed and shall have a "
                    "minimum bearing of 4 inches at each end unless a lesser bearing is justified by "
                    "engineering analysis."
                ),
            },
            {
                "id": "5.6.1",
                "heading": "5.6.1 — Mortar Joint Thickness for Architectural Veneer",
                "body": (
                    "Mortar joints in architectural thin veneer applications shall be a minimum of "
                    "3/8 inch and a maximum of 1/2 inch, measured at the narrowest point of the joint. "
                    "Joint thickness shall be verified by the installer prior to mortar set."
                ),
            },
            {
                "id": "5.6.2",
                "heading": "5.6.2 — Veneer Anchorage and Joint Reinforcement",
                "body": (
                    "[[ACC:P-2023-019]]Veneer anchors shall be spaced not more than 24 inches on "
                    "center vertically and 32 inches on center horizontally, except that in Wind "
                    "Exposure Category D, spacing shall not exceed 16 inches on center vertically and "
                    "24 inches on center horizontally.[[/ACC]] [[REV:P-2025-011]]Horizontal joint "
                    "reinforcement shall be provided at 16 inches on center in masonry veneer wythes, "
                    "except in Wind Exposure Category B, where reinforcement is not required.[[/REV]] "
                    "Anchors shall be corrosion-resistant per Section 2.4."
                ),
            },
        ],
    },
    {
        "id": "ch6",
        "number": "Chapter 6",
        "title": "Flashing & Waterproofing",
        "sections": [
            {
                "id": "6.1",
                "heading": "6.1 — General",
                "body": (
                    "Flashing shall be provided at all locations where moisture may enter the wall "
                    "system, including but not limited to the base of cavity walls, above and below "
                    "wall openings, and at roof-to-wall intersections."
                ),
            },
            {
                "id": "6.2",
                "heading": "6.2 — Flashing Materials",
                "body": (
                    "Flashing shall be corrosion-resistant metal, plastic, or rubberized asphalt "
                    "composite compatible with adjacent materials. Flashing shall extend through the "
                    "exterior face of the wall and terminate with a drip edge."
                ),
            },
            {
                "id": "6.3",
                "heading": "6.3 — End Dams",
                "body": (
                    "Flashing shall be turned up at both ends of each flashing run to form an end dam "
                    "not less than 1 inch in height, to prevent lateral migration of water off the ends "
                    "of the flashing."
                ),
            },
        ],
    },
    {
        "id": "ch7",
        "number": "Chapter 7",
        "title": "Seismic Design Provisions",
        "sections": [
            {
                "id": "7.1",
                "heading": "7.1 — General",
                "body": (
                    "Masonry structures shall be designed and detailed for the seismic design category "
                    "(SDC) assigned in accordance with the applicable building code. Additional "
                    "detailing requirements of this chapter apply based on that assigned category."
                ),
            },
            {
                "id": "7.2.3",
                "heading": "7.2.3 — Diaphragm Connections",
                "body": (
                    "[[ACC:P-2024-006]]In Seismic Design Category D and above, a continuous reinforced "
                    "bond beam shall be provided at every roof and floor diaphragm connection, detailed "
                    "in accordance with Section 7.4.[[/ACC]] In Seismic Design Categories A, B, and C, "
                    "bond beams at diaphragm connections are recommended but not required."
                ),
            },
            {
                "id": "7.3",
                "heading": "7.3 — Wall Anchorage to Diaphragms",
                "body": (
                    "Masonry walls shall be anchored to roof and floor diaphragms to resist the "
                    "out-of-plane forces specified in the applicable building code. Anchors shall be "
                    "embedded in grouted cells and spaced not more than 4 feet on center."
                ),
            },
            {
                "id": "7.4",
                "heading": "7.4 — Engineered Exceptions",
                "body": (
                    "Where an engineering analysis demonstrates that an alternative detailing approach "
                    "provides equivalent seismic performance to a prescriptive requirement of this "
                    "chapter, the alternative may be approved by the authority having jurisdiction on a "
                    "project-specific basis, subject to peer review for structures assigned to Risk "
                    "Category III or IV."
                ),
            },
        ],
    },
    {
        "id": "ch8",
        "number": "Chapter 8",
        "title": "Quality Assurance & Inspection",
        "sections": [
            {
                "id": "8.1",
                "heading": "8.1 — Levels of Quality Assurance",
                "body": (
                    "Masonry construction shall be subject to Level A, B, or C quality assurance as "
                    "defined in Table 8.1-A, based on Risk Category and Seismic Design Category. "
                    "Level C requires continuous special inspection of reinforcement placement and "
                    "grouting operations."
                ),
            },
            {
                "id": "8.2",
                "heading": "8.2 — Inspector Qualifications",
                "body": (
                    "Special inspectors shall be qualified in accordance with the applicable building "
                    "code and shall have documented experience in masonry construction inspection. "
                    "Inspection records shall be submitted to the authority having jurisdiction."
                ),
            },
            {
                "id": "8.3",
                "heading": "8.3 — Prism Testing",
                "body": (
                    "Where required by the quality assurance level, masonry prisms shall be "
                    "constructed and tested in accordance with ASTM C1314 to verify compliance with "
                    "the specified net area compressive strength (f'm)."
                ),
            },
        ],
    },
]

def get_all_proposals_by_status(status):
    return [p for p in PROPOSALS.values() if p["status"] == status]

def get_proposal(pid):
    return PROPOSALS.get(pid)


def _next_proposal_id():
    """Generate the next P-YYYY-NNN id for the current year."""
    year = date.today().year
    existing_nums = [
        int(pid.split("-")[-1])
        for pid in PROPOSALS.keys()
        if pid.startswith(f"P-{year}-")
    ]
    next_num = (max(existing_nums) + 1) if existing_nums else 1
    return f"P-{year}-{next_num:03d}"


def add_submitted_proposal(*, title, code_section, chapter_label, submitted_by,
                            summary, old_text, proposed_text, attachment_filename=None):
    """Create a new user-submitted proposal, defaulted to 'under_review',
    and insert it into the in-memory PROPOSALS store."""
    pid = _next_proposal_id()
    today = date.today().isoformat()

    opening_message = summary
    if attachment_filename:
        opening_message += f" (Attachment provided: {attachment_filename})"

    proposal = {
        "id": pid,
        "status": "under_review",
        "title": title,
        "code_section": code_section,
        "chapter": chapter_label or "Unassigned — new section proposed",
        "submitted_by": submitted_by,
        "date_submitted": today,
        "committee": "Pending Assignment",
        "stage": "Newly submitted — awaiting committee assignment",
        "summary": summary,
        "reasoning_so_far": "This proposal was just submitted through the public intake form and has not yet been reviewed by a committee.",
        "old_text": old_text or "(Not specified by proposer.)",
        "proposed_text": proposed_text,
        "attachment_filename": attachment_filename,
        "correspondence": [
            {"date": today, "author": submitted_by or "Anonymous Submitter",
             "role": "Proposer", "message": opening_message},
        ],
    }
    PROPOSALS[pid] = proposal
    return proposal
