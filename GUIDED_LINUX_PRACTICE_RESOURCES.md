# Guided Linux Practice Resources — November 8, 2026

> Purpose: return here when student financial-aid/loan funds arrive, or immediately for free practice. This is a resource bookmark and instructional plan, **not** a purchase authorization. Prices, offerings, availability and access tiers must be rechecked before purchase.

## Primary choice: LabEx

- Main site: https://labex.io/
- Pricing: https://labex.io/pricing
- Linux Journey on LabEx: https://labex.io/linuxjourney
- Why: browser-based terminal and guided, repeatable practical exercises. Check that specific Linux and RHCSA/RHEL labs desired are included in the subscription tier.
- November 8 research snapshot: annual LabEx Pro price was reported as about **US$99.90/year** (equivalent ~$8.33/month *when paid annually*, NOT a confirmed monthly payment option). Verify live pricing, tax, renewal terms, cancellation policy, and any restrictions before paying. Some free labs/VM launches may be available with limits; verify current free-tier terms.
- Purchase intention: author plans to consider a one-year subscription **after** loan/financial-aid funds actually arrive. No purchase yet made.

## Free/alternative hands-on learning resources

1. **Linux Foundation, Introduction to Linux (LFS101):** https://training.linuxfoundation.org/training/introduction-to-linux/ — free introductory course with hands-on labs/assignments; a ready-to-use hosted VM is not guaranteed for every lab, so check setup instructions. Better for structured fundamentals, not a complete RHCSA simulator.
2. **LinuxSim practice labs:** https://linuxsim.com/labs/ — short Linux exercise resource; verify current availability and free/paid access. Try for targeted repetition (file operations, permissions, grep/find).
3. **The Linux Camp — Linux Foundations:** https://thelinuxcamp.com/learn/linux-foundations — advertised guided browser-VM beginner exercises (previously described as 23 free guided labs); **confirm** present availability, VM access and pricing before relying on it.
4. **Linux Journey / LabEx:** https://labex.io/linuxjourney — check whether specific lessons and interactive labs are accessible free; the author reported paywall/access limitations, so **do not describe the entire experience as free**.

## Certification direction

- **RHCSA** (Red Hat Certified System Administrator) is a practical administration target. Official objectives and registration information should be checked directly on Red Hat's site: https://www.redhat.com/en/services/certification/rhcsa
- Continue practicing Debian/Ubuntu package tools for NOS-120, but separately practice RHEL-native workflows (especially DNF/RPM, services, users/groups, storage and SELinux) for RHCSA.
- The author also expressed interest in further Red Hat certification (spoken as “RHCA”); distinguish RHCA (Red Hat Certified Architect) from RHCE (Red Hat Certified Engineer) when eventually designing a credential path, without assuming either has been committed to yet.

## Teaching approach and LinuxLingo product implications

The author needs **teach → demonstrate → guided terminal attempt → independently execute → verify actual system state → repeat after a delay**, not more unscaffolded textbook reading or only multiple-choice recall. Use a real, disposable Linux VM; allow manual/help discovery during instruction, and measure independent recall separately. Use the established lab protocol: **read instruction → author's proposed command/guess → mentor validates reasoning → expand Cengage hint → execute → inspect output → harvest**. When the author says they don't recall, teach the command rather than repeatedly demand a guess.

Known learning gaps (November 8): identifying apt-cache subcommands (`pkgnames`, `show`, `depends`), apt-get operation (`install`), grep versus zgrep in package log searches, log locations, and relative path/working-directory requirements. Turn these into progressive hands-on practice; avoid assuming prerequisite syntax has been taught. Cengage verifier failure on Linux01 was resolved by generating the inventory in `/home/labuser` rather than `/home/labuser/Desktop`; document hidden path assumptions and confirm directory with `pwd` rather than punishing technically successful work. Guided lab completion is not independent mastery.

## Future action checklist

- [ ] Try representative free LabEx and alternative labs and judge *instructional quality*, not just number of exercises.
- [ ] When funds arrive, reconfirm annual price and whether RHCSA-relevant guided labs are included before purchasing.
- [ ] Choose a short, structured daily practice routine organized by skill, spaced recall, and measured command-line performance.
- [ ] Translate successful teaching patterns into LinuxLingo's future guided-terminal feature; today's MVP is not yet an integrated terminal coach.
