# 工具调用完整输出（原文）

源窗口：newpaper（`bc-ce9dbd5f-56a8-489e-90f8-8057905daaa2`）

导出时间：2026-10-25 16:21:28

主文档里这些调用只留了摘要行；下面是它们被截断前的完整输出。

---

## 1 · `pwsh` · 2026-10-25 00:38:02

参数：`pwsh Get-ChildItem records\queue -Filter '*pt*' | Select-Object Name, Length, LastWri…`

```text
[exit code: 0]

Name                                                           Length LastWriteTime      
----                                                           ------ -------------      
api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json                13814 2026/10/22 12:12:58
api_2026-10-22_xj-gpt-4.1-mini_203038_suite.json                 1352 2026/10/22 20:30:38
api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json                25490 2026/10/23 4:31:46 
api_2026-10-22_xj-gpt-4.1-mini_E10c_visual_score.out              528 2026/10/23 3:42:55 
api_2026-10-22_xj-gpt-4.1-mini_E10e_pointwise_L1_dev.out         3227 2026/10/23 3:26:14 
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev.out              3136 2026/10/22 11:20:55
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_rep1.out         3140 2026/10/22 22:50:38
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_v1.out           3144 2026/10/22 22:40:12
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_v2.out           3144 2026/10/22 22:45:08
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_test.out             5716 2026/10/22 12:12:02
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L2T_dev.out             2360 2026/10/23 3:43:22 
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L2T_test.out            2526 2026/10/23 3:44:29 
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L3H_dev.out             3142 2026/10/22 11:33:51
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L3_dev.out              3130 2026/10/22 11:27:10
api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L5_dev.out              3134 2026/10/22 11:40:17
api_2026-10-22_xj-gpt-4.1-mini_E15_harness_L1_dev40.out           820 2026/10/23 0:36:08 
api_2026-10-22_xj-gpt-4.1-mini_E15_harness_L2T_dev.out            797 2026/10/23 3:46:51 
api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L1_dev.out             2757 2026/10/22 23:47:53
api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L3_dev.out             2756 2026/10/22 23:28:22
api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L5_dev.out             2758 2026/10/22 23:09:32
api_2026-10-22_xj-gpt-4.1-mini_E5_closedbook.out                  630 2026/10/22 11:13:31
api_2026-10-22_xj-gpt-4.1-mini_E6_rerank_L1.out                   712 2026/10/23 4:28:20 
api_2026-10-22_xj-gpt-4.1-mini_E6_rerank_L5.out                   709 2026/10/23 4:31:46 
api_2026-10-22_xj-gpt-4.1-mini_E7_pair_verify_balanced.out       3411 2026/10/23 1:40:49 
api_2026-10-22_xj-gpt-4.1-mini_E8v4_L1_both_orders.out           2945 2026/10/23 4:17:57 
api_2026-10-22_xj-gpt-4.1-mini_E8v4_noevidence_maskcreator.out   2981 2026/10/23 0:22:15 
api_2026-10-22_xj-gpt-4.1-mini_E9_T5_profile_L1.out              1758 2026/10/23 4:23:18 
api_2026-10-22_xj-gpt-4.1-mini_suite.json                       25490 2026/10/23 4:31:46 
api_2026-10-22_xj-gpt-4.1-mini_suite.log                        23876 2026/10/23 4:31:46 
api_2026-10-22_xj-gpt-4.1_205353_suite.json                      1277 2026/10/22 20:53:53
api_2026-10-22_xj-gpt-4.1_214144_suite.json                     15150 2026/10/22 22:45:42
api_2026-10-22_xj-gpt-4.1_E10_agent_L1_dev.out                   3125 2026/10/22 21:54:13
api_2026-10-22_xj-gpt-4.1_E10_agent_L1_test.out                  5697 2026/10/22 22:44:54
api_2026-10-22_xj-gpt-4.1_E10_agent_L3H_dev.out                  3127 2026/10/22 22:11:53
api_2026-10-22_xj-gpt-4.1_E10_agent_L3_dev.out                   3124 2026/10/22 22:03:42
api_2026-10-22_xj-gpt-4.1_E10_agent_L5_dev.out                   3117 2026/10/22 22:22:45
api_2026-10-22_xj-gpt-4.1_E5_closedbook.out                       610 2026/10/22 21:47:09
api_2026-10-22_xj-gpt-4.1_suite.json                            15150 2026/10/22 22:45:42
api_2026-10-22_xj-gpt-4.1_suite.log                              6883 2026/10/22 22:45:42
api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json                16197 2026/10/22 22:13:32
api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L1_dev.out              3168 2026/10/22 21:10:52
api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L1_test.out             5752 2026/10/22 22:12:41
api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L3H_dev.out             3175 2026/10/22 21:29:04
api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L3_dev.out              3170 2026/10/22 21:20:06
api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L5_dev.out              3167 2026/10/22 21:40:14
api_2026-10-22_xj-gpt-5.4-mini_E5_closedbook.out                  661 2026/10/22 21:01:56
api_2026-10-22_xj-gpt-5.4-mini_suite.json                       16197 2026/10/22 22:13:32
api_2026-10-22_xj-gpt-5.4-mini_suite.log                         5685 2026/10/22 22:13:32
api_2026-10-22_xj-gpt-5.4_220008_suite.json                     15290 2026/10/22 22:59:14
api_2026-10-22_xj-gpt-5.4_E10_agent_L1_dev.out                   3122 2026/10/22 22:12:57
api_2026-10-22_xj-gpt-5.4_E10_agent_L1_test.out                  5697 2026/10/22 22:58:27
api_2026-10-22_xj-gpt-5.4_E10_agent_L3H_dev.out                  3128 2026/10/22 22:29:51
api_2026-10-22_xj-gpt-5.4_E10_agent_L3_dev.out                   3118 2026/10/22 22:23:38
api_2026-10-22_xj-gpt-5.4_E10_agent_L5_dev.out                   3124 2026/10/22 22:36:10
api_2026-10-22_xj-gpt-5.4_E5_closedbook.out                       608 2026/10/22 22:07:18
api_2026-10-22_xj-gpt-5.4_suite.json                            15290 2026/10/22 22:59:14
api_2026-10-22_xj-gpt-5.4_suite.log                              5664 2026/10/22 22:59:14
api_2026-10-23_xj-gpt-4.1-mini_235009_suite.json                 1352 2026/10/23 23:50:09
api_2026-10-23_xj-gpt-4.1-mini_235024_suite.json                 3431 2026/10/23 23:50:24
api_2026-10-23_xj-gpt-4.1-mini_suite.json                        3431 2026/10/23 23:50:24
api_2026-10-23_xj-gpt-4.1-mini_suite.log                         5425 2026/10/23 23:50:24
api_2026-10-23_xj-gpt-4.1_235019_suite.json                      1217 2026/10/23 23:50:19
api_2026-10-23_xj-gpt-4.1_suite.json                             1217 2026/10/23 23:50:19
api_2026-10-23_xj-gpt-4.1_suite.log                              1423 2026/10/23 23:50:19
api_2026-10-23_xj-gpt-5.4-mini_020546_suite.json                 8913 2026/10/23 3:00:07 
api_2026-10-23_xj-gpt-5.4-mini_235019_suite.json                 1334 2026/10/23 23:50:19
api_2026-10-23_xj-gpt-5.4-mini_E10v2_L1_dev.out                  3377 2026/10/23 2:14:12 
api_2026-10-23_xj-gpt-5.4-mini_E10v2_L1_test.out                 5964 2026/10/23 2:56:34 
api_2026-10-23_xj-gpt-5.4-mini_E10v2_L5_dev.out                  3381 2026/10/23 2:25:22 
api_2026-10-23_xj-gpt-5.4-mini_suite.json                        1334 2026/10/23 23:50:19
api_2026-10-23_xj-gpt-5.4-mini_suite.log                         4819 2026/10/23 23:50:19
api_2026-10-24_xj-gpt-4.1-mini_113934_suite.json                 5362 2026/10/24 11:47:41
api_2026-10-24_xj-gpt-4.1-mini_130731_suite.json                  711 2026/10/24 13:07:32
api_2026-10-24_xj-gpt-4.1-mini_201305_suite.json                 1352 2026/10/24 20:13:05
api_2026-10-24_xj-gpt-4.1-mini_201320_suite.json                 3431 2026/10/24 20:13:20
api_2026-10-24_xj-gpt-4.1-mini_E10_agent_L2Ttitle_dev.out        2760 2026/10/24 11:41:27
api_2026-10-24_xj-gpt-4.1-mini_E10_agent_L2Ttitle_test.out       3484 2026/10/24 11:47:27
api_2026-10-24_xj-gpt-4.1-mini_suite.json                        3431 2026/10/24 20:13:20
api_2026-10-24_xj-gpt-4.1-mini_suite.log                         8689 2026/10/24 20:13:20
api_2026-10-24_xj-gpt-4.1_040507_suite.json                      4309 2026/10/24 4:29:52 
api_2026-10-24_xj-gpt-4.1_115805_suite.json                      5259 2026/10/24 12:06:40
api_2026-10-24_xj-gpt-4.1_130741_suite.json                       616 2026/10/24 13:07:41
api_2026-10-24_xj-gpt-4.1_201315_suite.json                      1217 2026/10/24 20:13:15
api_2026-10-24_xj-gpt-4.1_204901_suite.json                      6376 2026/10/24 22:15:15
api_2026-10-24_xj-gpt-4.1_E10_agent_L2Ttitle_dev.out             2749 2026/10/24 12:00:08
api_2026-10-24_xj-gpt-4.1_E10_agent_L2Ttitle_test.out            3471 2026/10/24 12:06:28
api_2026-10-24_xj-gpt-4.1_E16_visual_L3_dev.out                  2739 2026/10/24 21:25:49
api_2026-10-24_xj-gpt-4.1_E16_visual_L5_dev.out                  2737 2026/10/24 4:27:53 
api_2026-10-24_xj-gpt-4.1_E8v4_noevidence_maskcreator.out        3025 2026/10/24 22:15:12
api_2026-10-24_xj-gpt-4.1_suite.json                             6376 2026/10/24 22:15:15
api_2026-10-24_xj-gpt-4.1_suite.log                             11051 2026/10/24 22:15:15
api_2026-10-24_xj-gpt-5.4-mini_120105_suite.json                 6168 2026/10/24 12:18:25
api_2026-10-24_xj-gpt-5.4-mini_130741_suite.json                  693 2026/10/24 13:07:41
api_2026-10-24_xj-gpt-5.4-mini_134727_suite.json                 4259 2026/10/24 16:13:22
api_2026-10-24_xj-gpt-5.4-mini_194019_suite.json                  681 2026/10/24 19:40:19
api_2026-10-24_xj-gpt-5.4-mini_201315_suite.json                 1334 2026/10/24 20:13:15
api_2026-10-24_xj-gpt-5.4-mini_E10_agent_L2Ttitle_dev.out        2792 2026/10/24 12:05:48
api_2026-10-24_xj-gpt-5.4-mini_E10_agent_L2Ttitle_test.out       3515 2026/10/24 12:18:09
api_2026-10-24_xj-gpt-5.4-mini_E10_agent_L3H_test.out            5808 2026/10/24 14:57:17
api_2026-10-24_xj-gpt-5.4-mini_E10_agent_L5_test.out             5800 2026/10/24 16:12:36
api_2026-10-24_xj-gpt-5.4-mini_suite.json                        1334 2026/10/24 20:13:15
api_2026-10-24_xj-gpt-5.4-mini_suite.log                         7972 2026/10/24 20:13:15
api_2026-10-24_xj-gpt-5.4_024906_suite.json                      6883 2026/10/24 3:37:20 
api_2026-10-24_xj-gpt-5.4_115122_suite.json                       777 2026/10/24 11:51:22
api_2026-10-24_xj-gpt-5.4_130736_suite.json                       777 2026/10/24 13:07:36
api_2026-10-24_xj-gpt-5.4_164053_suite.json                      5320 2026/10/24 17:20:25
api_2026-10-24_xj-gpt-5.4_194009_suite.json                       934 2026/10/24 19:40:09
api_2026-10-24_xj-gpt-5.4_194014_suite.json                       777 2026/10/24 19:40:14
api_2026-10-24_xj-gpt-5.4_203935_suite.json                      2960 2026/10/24 20:57:18
api_2026-10-24_xj-gpt-5.4_215306_suite.json                       934 2026/10/24 21:53:07
api_2026-10-24_xj-gpt-5.4_234810_suite.json                      1420 2026/10/24 23:56:35
api_2026-10-24_xj-gpt-5.4_E10_agent_L3H2_dev.out                 3326 2026/10/24 16:53:05
api_2026-10-24_xj-gpt-5.4_E10_agent_L3H_test.out                 5743 2026/10/24 3:12:13 
api_2026-10-24_xj-gpt-5.4_E10_agent_L5P_dev.out                  3332 2026/10/24 16:47:11
api_2026-10-24_xj-gpt-5.4_E10_agent_L5P_test.out                  239 2026/10/24 23:56:35
api_2026-10-24_xj-gpt-5.4_E10_agent_L5_test.out                  5739 2026/10/24 3:35:57 
api_2026-10-24_xj-gpt-5.4_E10_agent_L6_dev.out                   3328 2026/10/24 17:20:11
api_2026-10-24_xj-gpt-5.4_E17_open_L1_dev20.out                  3921 2026/10/24 20:57:18
api_2026-10-24_xj-gpt-5.4_suite.json                             1420 2026/10/24 23:56:35
api_2026-10-24_xj-gpt-5.4_suite.log                             13654 2026/10/24 23:56:35
api_2026-10-25_xj-gpt-4.1-mini_002023_suite.json                 1352 2026/10/25 0:20:24 
api_2026-10-25_xj-gpt-4.1-mini_002039_suite.json                 3431 2026/10/25 0:20:40 
api_2026-10-25_xj-gpt-4.1-mini_suite.json                        3431 2026/10/25 0:20:40 
api_2026-10-25_xj-gpt-4.1-mini_suite.log                         5425 2026/10/25 0:20:40 
api_2026-10-25_xj-gpt-4.1_002034_suite.json                      1217 2026/10/25 0:20:34 
api_2026-10-25_xj-gpt-4.1_suite.json                             1217 2026/10/25 0:20:34 
api_2026-10-25_xj-gpt-4.1_suite.log                              1423 2026/10/25 0:20:34 
api_2026-10-25_xj-gpt-5.4-mini_002034_suite.json                 1334 2026/10/25 0:20:34 
api_2026-10-25_xj-gpt-5.4-mini_suite.json                        1334 2026/10/25 0:20:34 
api_2026-10-25_xj-gpt-5.4-mini_suite.log                         1555 2026/10/25 0:20:34 
api_campaign_20261022_110753_stage3_xj-gpt-4.1-mini.out          5696 2026/10/22 12:12:58
api_campaign_20261022_123429_stage3_xj-gpt-4.1-mini.out             0 2026/10/22 12:34:29
api_campaign_20261022_123430_stage10_xj-gpt-5.4-mini.out            0 2026/10/22 12:34:30
api_campaign_20261022_123430_stage9_xj-gpt-4.1.out                  0 2026/10/22 12:34:30
api_campaign_20261022_123435_stage13_xj-gpt-4.1-mini.out            0 2026/10/22 12:34:35
api_campaign_20261022_123439_stage10_xj-gpt-5.4-mini.out            0 2026/10/22 12:34:39
api_campaign_20261022_123439_stage9_xj-gpt-4.1.out                  0 2026/10/22 12:34:39
api_campaign_20261022_123445_stage20_xj-gpt-4.1.out                 0 2026/10/22 12:34:45
api_campaign_20261022_203038_stage3_xj-gpt-4.1-mini.out          1573 2026/10/22 20:30:38
api_campaign_20261022_205353_stage9_xj-gpt-4.1.out               1483 2026/10/22 20:53:53
api_campaign_20261022_205358_stage10_xj-gpt-5.4-mini.out         5685 2026/10/22 22:13:32
api_campaign_20261022_214144_stage1_xj-gpt-4.1.out               5400 2026/10/22 22:45:42
api_campaign_20261022_220008_stage1_xj-gpt-5.4.out               5664 2026/10/22 22:59:14
api_campaign_20261022_223400_stage13_xj-gpt-4.1-mini.out        16607 2026/10/23 4:31:46 
api_campaign_20261023_020545_stage2_xj-gpt-5.4-mini.out          3264 2026/10/23 3:00:07 
api_campaign_20261023_063447_stage3_xj-gpt-4.1-mini.out             0 2026/10/23 6:34:47 
api_campaign_20261023_235009_stage3_xj-gpt-4.1-mini.out          1573 2026/10/23 23:50:09
api_campaign_20261023_235019_stage10_xj-gpt-5.4-mini.out         1555 2026/10/23 23:50:19
api_campaign_20261023_235019_stage9_xj-gpt-4.1.out               1423 2026/10/23 23:50:19
api_campaign_20261023_235024_stage13_xj-gpt-4.1-mini.out         3852 2026/10/23 23:50:24
api_campaign_20261024_024901_stage3_xj-gpt-5.4.out               2392 2026/10/24 3:37:20 
api_campaign_20261024_040451_stage20_xj-gpt-4.1.out              4086 2026/10/24 4:29:52 
api_campaign_20261024_113934_stage3_xj-gpt-4.1-mini.out          2370 2026/10/24 11:47:41
api_campaign_20261024_115122_stage3_xj-gpt-5.4.out                935 2026/10/24 11:51:22
api_campaign_20261024_115805_stage9_xj-gpt-4.1.out               2210 2026/10/24 12:06:40
api_campaign_20261024_120105_stage10_xj-gpt-5.4-mini.out         2354 2026/10/24 12:18:25
api_campaign_20261024_122728_stage6_xj-gpt-5.4-mini.out             0 2026/10/24 12:27:28
api_campaign_20261024_130731_stage3_xj-gpt-4.1-mini.out           894 2026/10/24 13:07:32
api_campaign_20261024_130736_stage3_xj-gpt-5.4.out                935 2026/10/24 13:07:36
api_campaign_20261024_130741_stage10_xj-gpt-5.4-mini.out          876 2026/10/24 13:07:41
api_campaign_20261024_130741_stage9_xj-gpt-4.1.out                784 2026/10/24 13:07:41
api_campaign_20261024_134726_stage6_xj-gpt-5.4-mini.out          2333 2026/10/24 16:13:22
api_campaign_20261024_164053_stage1_xj-gpt-5.4.out               3299 2026/10/24 17:20:25
api_campaign_20261024_194008_stage1_xj-gpt-5.4.out               1105 2026/10/24 19:40:09
api_campaign_20261024_194013_stage3_xj-gpt-5.4.out                935 2026/10/24 19:40:14
api_campaign_20261024_194018_stage6_xj-gpt-5.4-mini.out           854 2026/10/24 19:40:19
api_campaign_20261024_201305_stage3_xj-gpt-4.1-mini.out          1573 2026/10/24 20:13:05
api_campaign_20261024_201315_stage10_xj-gpt-5.4-mini.out         1555 2026/10/24 20:13:15
api_campaign_20261024_201315_stage9_xj-gpt-4.1.out               1423 2026/10/24 20:13:15
api_campaign_20261024_201320_stage13_xj-gpt-4.1-mini.out         3852 2026/10/24 20:13:20
api_campaign_20261024_203935_stage2_xj-gpt-5.4.out               1553 2026/10/24 20:57:18
api_campaign_20261024_204900_stage20_xj-gpt-4.1.out              2548 2026/10/24 22:15:15
api_campaign_20261024_215305_stage1_xj-gpt-5.4.out               1105 2026/10/24 21:53:07
api_campaign_20261024_234809_stage3_xj-gpt-5.4.out               1395 2026/10/24 23:56:35
api_campaign_20261025_002023_stage3_xj-gpt-4.1-mini.out          1573 2026/10/25 0:20:24 
api_campaign_20261025_002033_stage10_xj-gpt-5.4-mini.out         1555 2026/10/25 0:20:34 
api_campaign_20261025_002033_stage9_xj-gpt-4.1.out               1423 2026/10/25 0:20:34 
api_campaign_20261025_002038_stage13_xj-gpt-4.1-mini.out         3852 2026/10/25 0:20:40 
api_campaign_pt.lock                                               94 2026/10/25 0:37:31 
api_campaign_pt.log                                              1178 2026/10/25 0:20:28 
api_campaign_pt.state.json                                        158 2026/10/25 0:20:28 
api_campaign_pt_last.out                                            0 2026/10/25 0:20:27 
run_api_campaign_pt.cmd                                           317 2026/10/25 0:20:25 


--- pt log tail ---
2026-10-24 22:31:01 campaign start pid 61756 plan configs\campaign_s45_l5perm_test.json: 3 stages, max_parallel 2
2026-10-24 22:31:01 stage 1 started xj-gemini-3-pro pid 19292: E10_agent_L5P_test -> api_campaign_20261024_223101_stage1_xj-gemini-3-pro.out
2026-10-24 22:31:01 stage 2 started xj-claude-opus-4.6 pid 13372: E10_agent_L5P_test -> api_campaign_20261024_223101_stage2_xj-claude-opus-4.6.out
2026-10-24 23:48:09 stage 1 xj-gemini-3-pro finished rc=1
2026-10-24 23:48:09 stage 3 started xj-gpt-5.4 pid 34508: E10_agent_L5P_test -> api_campaign_20261024_234809_stage3_xj-gpt-5.4.out
2026-10-24 23:48:14 stage 2 xj-claude-opus-4.6 finished rc=1
2026-10-24 23:56:39 stage 3 xj-gpt-5.4 finished rc=1
2026-10-24 23:56:44 campaign done; complete=False attempt=1
2026-10-25 00:20:28 campaign start pid 59176 plan configs\campaign_s45_l5perm_test.json: 3 stages, max_parallel 2
2026-10-25 00:20:28 stage 1 started xj-gemini-3-pro pid 72232: E10_agent_L5P_test -> api_campaign_20261025_002028_stage1_xj-gemini-3-pro.out
2026-10-25 00:20:28 stage 2 started xj-claude-opus-4.6 pid 70852: E10_agent_L5P_test -> api_campaign_20261025_002028_stage2_xj-claude-opus-4.6.out
--- pt state ---
== api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-22T11:07:54+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "exp": "E5",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t0_closedbook",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 337.6,
   "run_dir": "20261022_110754_t0_closedbook_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 10950,
    "completion_tokens": 3604,
    "cost_usd": 0.0457,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E5_closedbook.out"
  },
  {
   "label": "E10_agent_L1_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 443.8,
   "run_dir": "20261022_111332_e10_agent_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156708,
    "completion_tokens": 7271,
    "cost_usd": 0.3344,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_111332.json",
    "2026-10-22_e10_shortlist_controls_20261022_111332.md",
    "2026-10-22_e10_shortlist_controls_20261022_111358.json",
    "2026-10-22_e10_shortlist_controls_20261022_111358.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_shortlist_shortcuts.json",
    "2026-10-22_shortlist_shortcuts.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3"
   ],
   "rc": 0,
   "seconds": 352.5,
   "run_dir": "20261022_112119_e10_agent_L3_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 142696,
    "completion_tokens": 7275,
    "cost_usd": 0.3092,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L1_xj-qwen3.5-397b.json",
    "2026-10-22_e10_regate_L1_xj-qwen3.5-397b.md",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_111353.json",
    "2026-10-22_e10_shortlist_controls_20261022_111353.md",
    "2026-10-22_e10_shortlist_controls_20261022_111422.json",
    "2026-10-22_e10_shortlist_controls_20261022_111422.md",
    "2026-10-22_e10_shortlist_controls_20261022_112053.json",
    "2026-10-22_e10_shortlist_controls_20261022_112053.md",
    "2026-10-22_e10_shortlist_controls_20261022_112119.json",
    "2026-10-22_e10_shortlist_controls_20261022_112119.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_llm_reunion_agent_L1_xj-qwen3.5-397b.json",
    "2026-10-22_llm_reunion_agent_L1_xj-qwen3.5-397b.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-flash.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1-mini.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1-mini.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L3_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3H_dev",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 380.4,
   "run_dir": "20261022_112731_e10_agent_L3-H_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 138786,
    "completion_tokens": 5829,
    "cost_usd": 0.2918,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L3-H_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L3-H_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_regate_L3_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L3_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L3_xj-qwen3.5-397b.json",
    "2026-10-22_e10_regate_L3_xj-qwen3.5-397b.md",
    "2026-10-22_e10_shortlist_controls_20261022_112229.json",
    "2026-10-22_e10_shortlist_controls_20261022_112229.md",
    "2026-10-22_e10_shortlist_controls_20261022_112318.json",
    "2026-10-22_e10_shortlist_controls_20261022_112318.md",
    "2026-10-22_e10_shortlist_controls_20261022_112647.json",
    "2026-10-22_e10_shortlist_controls_20261022_112647.md",
    "2026-10-22_e10_shortlist_controls_20261022_112731.json",
    "2026-10-22_e10_shortlist_controls_20261022_112731.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gemini-2.5-flash.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1-mini.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1-mini.md",
    "2026-10-22_llm_reunion_agent_L3_xj-claude-haiku-4.5.json",
    "2026-10-22_llm_reunion_agent_L3_xj-claude-haiku-4.5.md",
    "2026-10-22_llm_reunion_agent_L3_xj-qwen3.5-397b.json",
    "2026-10-22_llm_reunion_agent_L3_xj-qwen3.5-397b.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L3H_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_112731_e10_agent_L3-H_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_112731_e10_agent_L3-H_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 368.5,
   "run_dir": "20261022_113410_e10_agent_L5_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 96610,
    "completion_tokens": 3910,
    "cost_usd": 0.202,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L3-H_xj-qwen3.5-397b.json",
    "2026-10-22_e10_regate_L3-H_xj-qwen3.5-397b.md",
    "2026-10-22_e10_regate_L5_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L5_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_113035.json",
    "2026-10-22_e10_shortlist_controls_20261022_113035.md",
    "2026-10-22_e10_shortlist_controls_20261022_113317.json",
    "2026-10-22_e10_shortlist_controls_20261022_113317.md",
    "2026-10-22_e10_shortlist_controls_20261022_113410.json",
    "2026-10-22_e10_shortlist_controls_20261022_113410.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-qwen3.5-397b.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-qwen3.5-397b.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gemini-2.5-flash.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1-mini.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1-mini.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L5_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 1885.6,
   "run_dir": "20261022_114037_e10_agent_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 594852,
    "completion_tokens": 27320,
    "cost_usd": 1.2537,
    "cache_hits": 3,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 294
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L1_test_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_regate_L3-H_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L3-H_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L5_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L5_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L5_xj-qwen3.5-397b.json",
    "2026-10-22_e10_regate_L5_xj-qwen3.5-397b.md",
    "2026-10-22_e10_shortlist_controls_20261022_113235.json",
    "2026-10-22_e10_shortlist_controls_20261022_113235.md",
    "2026-10-22_e10_shortlist_controls_20261022_113825.json",
    "2026-10-22_e10_shortlist_controls_20261022_113825.md",
    "2026-10-22_e10_shortlist_controls_20261022_114008.json",
    "2026-10-22_e10_shortlist_controls_20261022_114008.md",
    "2026-10-22_e10_shortlist_controls_20261022_114037.json",
    "2026-10-22_e10_shortlist_controls_20261022_114037.md",
    "2026-10-22_e10_shortlist_controls_20261022_114155.json",
    "2026-10-22_e10_shortlist_controls_20261022_114155.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gemini-2.5-flash.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1-mini.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1-mini.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-claude-haiku-4.5.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-claude-haiku-4.5.md",
    "2026-10-22_llm_reunion_agent_L5_xj-claude-haiku-4.5.json",
    "2026-10-22_llm_reunion_agent_L5_xj-claude-haiku-4.5.md",
    "2026-10-22_llm_reunion_agent_L5_xj-qwen3.5-397b.json",
    "2026-10-22_llm_reunion_agent_L5_xj-qwen3.5-397b.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_114037_e10_agent_L1_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_114037_e10_agent_L1_xj-gpt-4.1-mini (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-22T12:12:58+08:00"
}
== api_2026-10-22_xj-gpt-4.1-mini_203038_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-22T20:30:38+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_110754_t0_closedbook_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112731_e10_agent_L3-H_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_114037_e10_agent_L1_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-22T20:30:38+08:00"
}
== api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-22T22:34:01+08:00",
 "jobs": [
  {
   "label": "E10_agent_L1_dev_v1",
   "exp": "E10P",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1",
    "--prompt-variant",
    "v1"
   ],
   "rc": 0,
   "seconds": 371.5,
   "run_dir": "20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156948,
    "completion_tokens": 8431,
    "cost_usd": 0.3432,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_223020.json",
    "2026-10-22_e10_shortlist_controls_20261022_223020.md",
    "2026-10-22_e10_shortlist_controls_20261022_223210.json",
    "2026-10-22_e10_shortlist_controls_20261022_223210.md",
    "2026-10-22_e10_shortlist_controls_20261022_223403.json",
    "2026-10-22_e10_shortlist_controls_20261022_223403.md",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_v1.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_dev_v2",
   "exp": "E10P",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1",
    "--prompt-variant",
    "v2"
   ],
   "rc": 0,
   "seconds": 284.0,
   "run_dir": "20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156788,
    "completion_tokens": 4752,
    "cost_usd": 0.3164,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_commons_identity.json",
    "2026-10-22_commons_identity.md",
    "2026-10-22_commons_views.json",
    "2026-10-22_custody_events.json",
    "2026-10-22_custody_events.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_224025.json",
    "2026-10-22_e10_shortlist_controls_20261022_224025.md",
    "2026-10-22_enrich_records.json",
    "2026-10-22_extra_views.json",
    "2026-10-22_fact_cards.json",
    "2026-10-22_fact_cards.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.md",
    "2026-10-22_media_integrity.json",
    "2026-10-22_media_integrity.md",
    "2026-10-22_media_usability.json",
    "2026-10-22_media_usability.md",
    "2026-10-22_membership_evidence.json",
    "2026-10-22_membership_evidence.md",
    "2026-10-22_near_duplicates.json",
    "2026-10-22_near_duplicates.md",
    "2026-10-22_nga_views.json",
    "2026-10-22_quality_audit.json",
    "2026-10-22_quality_audit.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md",
    "2026-10-22_shortlist_shortcuts.json",
    "2026-10-22_shortlist_shortcuts.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md",
    "2026-10-22_text_screen.json",
    "2026-10-22_text_screen.md",
    "2026-10-22_wikidata_deep.json",
    "2026-10-22_wikidata_deep.md",
    "2026-10-22_wikipedia_dump.json"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_v2.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_dev_rep1",
   "exp": "E10P",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1",
    "--replicate",
    "1"
   ],
   "rc": 0,
   "seconds": 316.9,
   "run_dir": "20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156708,
    "completion_tokens": 6844,
    "cost_usd": 0.3313,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_222258.json",
    "2026-10-22_e10_shortlist_controls_20261022_222258.md",
    "2026-10-22_e10_shortlist_controls_20261022_224522.json",
    "2026-10-22_e10_shortlist_controls_20261022_224522.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_rep1.md",
    "2026-10-22_oa_fulltext.json"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_rep1.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1 (rc=0)"
   ]
  },
  {
   "label": "E16_visual_L5_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--from-run",
    "20261013_233240_e10_agent_L5_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 1122.3,
   "run_dir": "20261022_225050_e16_visual_L5_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 488229,
    "completion_tokens": 11861,
    "cost_usd": 0.9642,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_223622.json",
    "2026-10-22_e10_shortlist_controls_20261022_223622.md",
    "2026-10-22_e16_visual_L1_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L1_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_e16_visual_L5_dev_xj-gpt-4.1-mini.json",
    "2026-10-22_e16_visual_L5_dev_xj-gpt-4.1-mini.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L5_dev.out"
  },
  {
   "label": "E16_visual_L3_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--from-run",
    "20261013_225051_e10_agent_L3_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 1130.7,
   "run_dir": "20261022_230933_e16_visual_L3_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 514277,
    "completion_tokens": 12384,
    "cost_usd": 1.0149,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-22_cf_forced_choice_analysis_xj-gemini-2.5-flashv4_noevidence_maskcreator.json",
    "2026-10-22_cf_forced_choice_analysis_xj-gemini-2.5-flashv4_noevidence_maskcreator.md",
    "2026-10-22_cf_forced_choice_xj-gemini-2.5-flashv4_noevidence_maskcreator.json",
    "2026-10-22_cf_forced_choice_xj-gemini-2.5-flashv4_noevidence_maskcreator.md",
    "2026-10-22_e10_regate_L1_xj-claude-opus-4.6.json",
    "2026-10-22_e10_regate_L1_xj-claude-opus-4.6.md",
    "2026-10-22_e10_regate_L3-H_xj-gemini-2.5-pro.json",
    "2026-10-22_e10_regate_L3-H_xj-gemini-2.5-pro.md",
    "2026-10-22_e10_shortlist_controls_20261022_223157.json",
    "2026-10-22_e10_shortlist_controls_20261022_223157.md",
    "2026-10-22_e10_shortlist_controls_20261022_231234.json",
    "2026-10-22_e10_shortlist_controls_20261022_231234.md",
    "2026-10-22_e16_visual_L3_dev_xj-gpt-4.1-mini.json",
    "2026-10-22_e16_visual_L3_dev_xj-gpt-4.1-mini.md",
    "2026-10-22_e16_visual_L5_dev_xj-claude-haiku-4.5.json",
    "2026-10-22_e16_visual_L5_dev_xj-claude-haiku-4.5.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-opus-4.6.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-opus-4.6.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gemini-2.5-pro.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gemini-2.5-pro.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L3_dev.out"
  },
  {
   "label": "E16_visual_L1_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--from-run",
    "20261013_200012_e10_agent_L1_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 1170.6,
   "run_dir": "20261022_232828_e16_visual_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 514034,
    "completion_tokens": 14446,
    "cost_usd": 1.0293,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L3_xj-claude-opus-4.6.json",
    "2026-10-22_e10_regate_L3_xj-claude-opus-4.6.md",
    "2026-10-22_e10_shortlist_controls_20261022_232654.json",
    "2026-10-22_e10_shortlist_controls_20261022_232654.md",
    "2026-10-22_e16_visual_L1_dev_xj-gpt-4.1-mini.json",
    "2026-10-22_e16_visual_L1_dev_xj-gpt-4.1-mini.md",
    "2026-10-22_llm_reunion_agent_L3_xj-claude-opus-4.6.json",
    "2026-10-22_llm_reunion_agent_L3_xj-claude-opus-4.6.md",
    "2026-10-22_quality_audit.json",
    "2026-10-22_quality_audit.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L1_dev.out"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "exp": "E8",
   "argv": [
    "scripts/llm_cf_forced_choice.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--n",
    "100",
    "--withhold-evidence",
    "--mask-creator",
    "--both-orders",
    "--tag",
    "v4"
   ],
   "rc": 0,
   "seconds": 2060.5,
   "run_dir": "20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator",
   "run_json": true,
   "stats": {
    "calls": 600,
    "usage_records": 600,
    "prompt_tokens": 155678,
    "completion_tokens": 25376,
    "cost_usd": 0.4601,
    "cache_hits": 4,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 600,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 600
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash-thinking.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash-thinking.md",
    "2026-10-22_e10_shortlist_controls_20261022_230852.json",
    "2026-10-22_e10_shortlist_controls_20261022_230852.md",
    "2026-10-22_e16_visual_L3_dev_xj-claude-haiku-4.5.json",
    "2026-10-22_e16_visual_L3_dev_xj-claude-haiku-4.5.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash-thinking.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash-thinking.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E8v4_noevidence_maskcreator.out",
   "follow_up": [
    "scripts/llm_cf_forced_choice.py --analyze-run 20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator (rc=0)"
   ]
  },
  {
   "label": "E15_harness_L1_dev40",
   "exp": "E15",
   "argv": [
    "scripts/deep_research_harness.py",
    "--policy",
    "llm",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--level",
    "L1",
    "--split",
    "dev",
    "--limit",
    "40",
    "--max-steps",
    "30",
    "--max-tokens",
    "200"
   ],
   "rc": 0,
   "seconds": 833.4,
   "run_dir": "20261023_002216_harness_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 40,
    "usage_records": 295,
    "prompt_tokens": 332674,
    "completion_tokens": 9337,
    "cost_usd": 0.631,
    "cache_hits": 47,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 295,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 295
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E15_harness_L1_dev40.out"
  },
  {
   "label": "E7_pair_verify_balanced",
   "exp": "E7",
   "argv": [
    "scripts/mllm_pair_verify.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--n",
    "150",
    "--balance-source",
    "--score-only",
    "--conditions",
    "V0,V4"
   ],
   "rc": 0,
   "seconds": 3880.7,
   "run_dir": "20261023_003611_c4_pair_verify_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 754,
    "usage_records": 754,
    "prompt_tokens": 767175,
    "completion_tokens": 754,
    "cost_usd": 1.3864,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 754,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 754
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E7_pair_verify_balanced.out"
  },
  {
   "label": "E10e_pointwise_L1_dev",
   "exp": "E10e",
   "argv": [
    "scripts/llm_pointwise_rerank.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--from-run",
    "20261022_111332_e10_agent_L1_xj-gpt-4.1-mini",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 6323.0,
   "run_dir": "20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 2344,
    "prompt_tokens": 576534,
    "completion_tokens": 2344,
    "cost_usd": 0.9899,
    "cache_hits": 135,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 2344,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 2344
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10e_pointwise_L1_dev.out"
  },
  {
   "label": "E10c_visual_score",
   "exp": "E10c",
   "argv": [
    "scripts/e10_visual_gate.py",
    "--score",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--runs",
    "20261022_111332_e10_agent_L1_xj-gpt-4.1-mini",
    "20261022_112119_e10_agent_L3_xj-gpt-4.1-mini",
    "20261022_113410_e10_agent_L5_xj-gpt-4.1-mini"
   ],
   "rc": 0,
   "seconds": 1000.9,
   "run_dir": "20261023_032614_e10c_visual_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 229,
    "usage_records": 229,
    "prompt_tokens": 230165,
    "completion_tokens": 229,
    "cost_usd": 0.3885,
    "cache_hits": 14,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 229,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 229
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10c_visual_score.out",
   "follow_up": [
    "scripts/e10_visual_gate.py --replay --runs 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini --visual-run 20261023_032614_e10c_visual_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L2T_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 15.3,
   "run_dir": "20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 5,
    "usage_records": 5,
    "prompt_tokens": 8652,
    "completion_tokens": 476,
    "cost_usd": 0.019,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 5,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 5
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L2T_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L2T_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 64.6,
   "run_dir": "20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 17,
    "usage_records": 17,
    "prompt_tokens": 32813,
    "completion_tokens": 1871,
    "cost_usd": 0.0725,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 17,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 17
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L2T_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E15_harness_L2T_dev",
   "exp": "E15",
   "argv": [
    "scripts/deep_research_harness.py",
    "--policy",
    "llm",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--level",
    "L2-T",
    "--split",
    "dev",
    "--limit",
    "0",
    "--max-steps",
    "30",
    "--max-tokens",
    "200"
   ],
   "rc": 0,
   "seconds": 130.0,
   "run_dir": "20261023_034446_harness_L2T_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 5,
    "usage_records": 39,
    "prompt_tokens": 34418,
    "completion_tokens": 1043,
    "cost_usd": 0.0667,
    "cache_hits": 4,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 39,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 39
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E15_harness_L2T_dev.out"
  },
  {
   "label": "E8v4_L1_both_orders",
   "exp": "E8",
   "argv": [
    "scripts/llm_cf_forced_choice.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--n",
    "100",
    "--both-orders",
    "--tag",
    "v4"
   ],
   "rc": 0,
   "seconds": 1866.3,
   "run_dir": "20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4",
   "run_json": true,
   "stats": {
    "calls": 600,
    "usage_records": 600,
    "prompt_tokens": 201242,
    "completion_tokens": 25883,
    "cost_usd": 0.5468,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 600,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 600
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E8v4_L1_both_orders.out",
   "follow_up": [
    "scripts/llm_cf_forced_choice.py --analyze-run 20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4 (rc=0)"
   ]
  },
  {
   "label": "E9_T5_profile_L1",
   "exp": "E9",
   "argv": [
    "scripts/llm_t5_profile.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--n",
    "80",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 320.4,
   "run_dir": "20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 36605,
    "completion_tokens": 8101,
    "cost_usd": 0.1219,
    "cache_hits": 1,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E9_T5_profile_L1.out",
   "follow_up": [
    "scripts/llm_t5_profile.py --replay 20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E6_rerank_L1",
   "exp": "E6",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t1_rerank",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--level",
    "L1",
    "--split",
    "dev",
    "--limit",
    "40",
    "--k",
    "30",
    "--max-tokens",
    "300"
   ],
   "rc": 0,
   "seconds": 177.5,
   "run_dir": "20261023_042523_t1_rerank_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 40,
    "usage_records": 40,
    "prompt_tokens": 81366,
    "completion_tokens": 10672,
    "cost_usd": 0.2233,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 40,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 40
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E6_rerank_L1.out"
  },
  {
   "label": "E6_rerank_L5",
   "exp": "E6",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t1_rerank",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--level",
    "L5",
    "--split",
    "dev",
    "--limit",
    "40",
    "--k",
    "30",
    "--max-tokens",
    "300"
   ],
   "rc": 0,
   "seconds": 205.7,
   "run_dir": "20261023_042821_t1_rerank_L5_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 40,
    "usage_records": 40,
    "prompt_tokens": 49266,
    "completion_tokens": 9648,
    "cost_usd": 0.1581,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 40,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 40
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E6_rerank_L5.out"
  }
 ],
 "finished": "2026-10-23T04:31:46+08:00"
}
== api_2026-10-22_xj-gpt-4.1-mini_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-22T22:34:01+08:00",
 "jobs": [
  {
   "label": "E10_agent_L1_dev_v1",
   "exp": "E10P",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1",
    "--prompt-variant",
    "v1"
   ],
   "rc": 0,
   "seconds": 371.5,
   "run_dir": "20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156948,
    "completion_tokens": 8431,
    "cost_usd": 0.3432,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_223020.json",
    "2026-10-22_e10_shortlist_controls_20261022_223020.md",
    "2026-10-22_e10_shortlist_controls_20261022_223210.json",
    "2026-10-22_e10_shortlist_controls_20261022_223210.md",
    "2026-10-22_e10_shortlist_controls_20261022_223403.json",
    "2026-10-22_e10_shortlist_controls_20261022_223403.md",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_v1.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_dev_v2",
   "exp": "E10P",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1",
    "--prompt-variant",
    "v2"
   ],
   "rc": 0,
   "seconds": 284.0,
   "run_dir": "20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156788,
    "completion_tokens": 4752,
    "cost_usd": 0.3164,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_commons_identity.json",
    "2026-10-22_commons_identity.md",
    "2026-10-22_commons_views.json",
    "2026-10-22_custody_events.json",
    "2026-10-22_custody_events.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_224025.json",
    "2026-10-22_e10_shortlist_controls_20261022_224025.md",
    "2026-10-22_enrich_records.json",
    "2026-10-22_extra_views.json",
    "2026-10-22_fact_cards.json",
    "2026-10-22_fact_cards.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.md",
    "2026-10-22_media_integrity.json",
    "2026-10-22_media_integrity.md",
    "2026-10-22_media_usability.json",
    "2026-10-22_media_usability.md",
    "2026-10-22_membership_evidence.json",
    "2026-10-22_membership_evidence.md",
    "2026-10-22_near_duplicates.json",
    "2026-10-22_near_duplicates.md",
    "2026-10-22_nga_views.json",
    "2026-10-22_quality_audit.json",
    "2026-10-22_quality_audit.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md",
    "2026-10-22_shortlist_shortcuts.json",
    "2026-10-22_shortlist_shortcuts.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md",
    "2026-10-22_text_screen.json",
    "2026-10-22_text_screen.md",
    "2026-10-22_wikidata_deep.json",
    "2026-10-22_wikidata_deep.md",
    "2026-10-22_wikipedia_dump.json"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_v2.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_dev_rep1",
   "exp": "E10P",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1",
    "--replicate",
    "1"
   ],
   "rc": 0,
   "seconds": 316.9,
   "run_dir": "20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156708,
    "completion_tokens": 6844,
    "cost_usd": 0.3313,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_222258.json",
    "2026-10-22_e10_shortlist_controls_20261022_222258.md",
    "2026-10-22_e10_shortlist_controls_20261022_224522.json",
    "2026-10-22_e10_shortlist_controls_20261022_224522.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_rep1.md",
    "2026-10-22_oa_fulltext.json"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L1_dev_rep1.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1 (rc=0)"
   ]
  },
  {
   "label": "E16_visual_L5_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--from-run",
    "20261013_233240_e10_agent_L5_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 1122.3,
   "run_dir": "20261022_225050_e16_visual_L5_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 488229,
    "completion_tokens": 11861,
    "cost_usd": 0.9642,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_223622.json",
    "2026-10-22_e10_shortlist_controls_20261022_223622.md",
    "2026-10-22_e16_visual_L1_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L1_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_e16_visual_L5_dev_xj-gpt-4.1-mini.json",
    "2026-10-22_e16_visual_L5_dev_xj-gpt-4.1-mini.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L5_dev.out"
  },
  {
   "label": "E16_visual_L3_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--from-run",
    "20261013_225051_e10_agent_L3_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 1130.7,
   "run_dir": "20261022_230933_e16_visual_L3_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 514277,
    "completion_tokens": 12384,
    "cost_usd": 1.0149,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-22_cf_forced_choice_analysis_xj-gemini-2.5-flashv4_noevidence_maskcreator.json",
    "2026-10-22_cf_forced_choice_analysis_xj-gemini-2.5-flashv4_noevidence_maskcreator.md",
    "2026-10-22_cf_forced_choice_xj-gemini-2.5-flashv4_noevidence_maskcreator.json",
    "2026-10-22_cf_forced_choice_xj-gemini-2.5-flashv4_noevidence_maskcreator.md",
    "2026-10-22_e10_regate_L1_xj-claude-opus-4.6.json",
    "2026-10-22_e10_regate_L1_xj-claude-opus-4.6.md",
    "2026-10-22_e10_regate_L3-H_xj-gemini-2.5-pro.json",
    "2026-10-22_e10_regate_L3-H_xj-gemini-2.5-pro.md",
    "2026-10-22_e10_shortlist_controls_20261022_223157.json",
    "2026-10-22_e10_shortlist_controls_20261022_223157.md",
    "2026-10-22_e10_shortlist_controls_20261022_231234.json",
    "2026-10-22_e10_shortlist_controls_20261022_231234.md",
    "2026-10-22_e16_visual_L3_dev_xj-gpt-4.1-mini.json",
    "2026-10-22_e16_visual_L3_dev_xj-gpt-4.1-mini.md",
    "2026-10-22_e16_visual_L5_dev_xj-claude-haiku-4.5.json",
    "2026-10-22_e16_visual_L5_dev_xj-claude-haiku-4.5.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-opus-4.6.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-opus-4.6.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gemini-2.5-pro.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gemini-2.5-pro.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L3_dev.out"
  },
  {
   "label": "E16_visual_L1_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--from-run",
    "20261013_200012_e10_agent_L1_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 1170.6,
   "run_dir": "20261022_232828_e16_visual_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 514034,
    "completion_tokens": 14446,
    "cost_usd": 1.0293,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L3_xj-claude-opus-4.6.json",
    "2026-10-22_e10_regate_L3_xj-claude-opus-4.6.md",
    "2026-10-22_e10_shortlist_controls_20261022_232654.json",
    "2026-10-22_e10_shortlist_controls_20261022_232654.md",
    "2026-10-22_e16_visual_L1_dev_xj-gpt-4.1-mini.json",
    "2026-10-22_e16_visual_L1_dev_xj-gpt-4.1-mini.md",
    "2026-10-22_llm_reunion_agent_L3_xj-claude-opus-4.6.json",
    "2026-10-22_llm_reunion_agent_L3_xj-claude-opus-4.6.md",
    "2026-10-22_quality_audit.json",
    "2026-10-22_quality_audit.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E16_visual_L1_dev.out"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "exp": "E8",
   "argv": [
    "scripts/llm_cf_forced_choice.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--n",
    "100",
    "--withhold-evidence",
    "--mask-creator",
    "--both-orders",
    "--tag",
    "v4"
   ],
   "rc": 0,
   "seconds": 2060.5,
   "run_dir": "20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator",
   "run_json": true,
   "stats": {
    "calls": 600,
    "usage_records": 600,
    "prompt_tokens": 155678,
    "completion_tokens": 25376,
    "cost_usd": 0.4601,
    "cache_hits": 4,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 600,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 600
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash-thinking.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash-thinking.md",
    "2026-10-22_e10_shortlist_controls_20261022_230852.json",
    "2026-10-22_e10_shortlist_controls_20261022_230852.md",
    "2026-10-22_e16_visual_L3_dev_xj-claude-haiku-4.5.json",
    "2026-10-22_e16_visual_L3_dev_xj-claude-haiku-4.5.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash-thinking.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash-thinking.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E8v4_noevidence_maskcreator.out",
   "follow_up": [
    "scripts/llm_cf_forced_choice.py --analyze-run 20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator (rc=0)"
   ]
  },
  {
   "label": "E15_harness_L1_dev40",
   "exp": "E15",
   "argv": [
    "scripts/deep_research_harness.py",
    "--policy",
    "llm",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--level",
    "L1",
    "--split",
    "dev",
    "--limit",
    "40",
    "--max-steps",
    "30",
    "--max-tokens",
    "200"
   ],
   "rc": 0,
   "seconds": 833.4,
   "run_dir": "20261023_002216_harness_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 40,
    "usage_records": 295,
    "prompt_tokens": 332674,
    "completion_tokens": 9337,
    "cost_usd": 0.631,
    "cache_hits": 47,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 295,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 295
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E15_harness_L1_dev40.out"
  },
  {
   "label": "E7_pair_verify_balanced",
   "exp": "E7",
   "argv": [
    "scripts/mllm_pair_verify.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--n",
    "150",
    "--balance-source",
    "--score-only",
    "--conditions",
    "V0,V4"
   ],
   "rc": 0,
   "seconds": 3880.7,
   "run_dir": "20261023_003611_c4_pair_verify_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 754,
    "usage_records": 754,
    "prompt_tokens": 767175,
    "completion_tokens": 754,
    "cost_usd": 1.3864,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 754,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 754
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E7_pair_verify_balanced.out"
  },
  {
   "label": "E10e_pointwise_L1_dev",
   "exp": "E10e",
   "argv": [
    "scripts/llm_pointwise_rerank.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--from-run",
    "20261022_111332_e10_agent_L1_xj-gpt-4.1-mini",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 6323.0,
   "run_dir": "20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 2344,
    "prompt_tokens": 576534,
    "completion_tokens": 2344,
    "cost_usd": 0.9899,
    "cache_hits": 135,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 2344,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 2344
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10e_pointwise_L1_dev.out"
  },
  {
   "label": "E10c_visual_score",
   "exp": "E10c",
   "argv": [
    "scripts/e10_visual_gate.py",
    "--score",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--runs",
    "20261022_111332_e10_agent_L1_xj-gpt-4.1-mini",
    "20261022_112119_e10_agent_L3_xj-gpt-4.1-mini",
    "20261022_113410_e10_agent_L5_xj-gpt-4.1-mini"
   ],
   "rc": 0,
   "seconds": 1000.9,
   "run_dir": "20261023_032614_e10c_visual_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 229,
    "usage_records": 229,
    "prompt_tokens": 230165,
    "completion_tokens": 229,
    "cost_usd": 0.3885,
    "cache_hits": 14,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 229,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 229
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10c_visual_score.out",
   "follow_up": [
    "scripts/e10_visual_gate.py --replay --runs 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini --visual-run 20261023_032614_e10c_visual_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L2T_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 15.3,
   "run_dir": "20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 5,
    "usage_records": 5,
    "prompt_tokens": 8652,
    "completion_tokens": 476,
    "cost_usd": 0.019,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 5,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 5
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L2T_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L2T_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 64.6,
   "run_dir": "20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 17,
    "usage_records": 17,
    "prompt_tokens": 32813,
    "completion_tokens": 1871,
    "cost_usd": 0.0725,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 17,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 17
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E10_agent_L2T_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E15_harness_L2T_dev",
   "exp": "E15",
   "argv": [
    "scripts/deep_research_harness.py",
    "--policy",
    "llm",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--level",
    "L2-T",
    "--split",
    "dev",
    "--limit",
    "0",
    "--max-steps",
    "30",
    "--max-tokens",
    "200"
   ],
   "rc": 0,
   "seconds": 130.0,
   "run_dir": "20261023_034446_harness_L2T_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 5,
    "usage_records": 39,
    "prompt_tokens": 34418,
    "completion_tokens": 1043,
    "cost_usd": 0.0667,
    "cache_hits": 4,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 39,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 39
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E15_harness_L2T_dev.out"
  },
  {
   "label": "E8v4_L1_both_orders",
   "exp": "E8",
   "argv": [
    "scripts/llm_cf_forced_choice.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--n",
    "100",
    "--both-orders",
    "--tag",
    "v4"
   ],
   "rc": 0,
   "seconds": 1866.3,
   "run_dir": "20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4",
   "run_json": true,
   "stats": {
    "calls": 600,
    "usage_records": 600,
    "prompt_tokens": 201242,
    "completion_tokens": 25883,
    "cost_usd": 0.5468,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 600,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 600
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E8v4_L1_both_orders.out",
   "follow_up": [
    "scripts/llm_cf_forced_choice.py --analyze-run 20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4 (rc=0)"
   ]
  },
  {
   "label": "E9_T5_profile_L1",
   "exp": "E9",
   "argv": [
    "scripts/llm_t5_profile.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--n",
    "80",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 320.4,
   "run_dir": "20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 36605,
    "completion_tokens": 8101,
    "cost_usd": 0.1219,
    "cache_hits": 1,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 80
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E9_T5_profile_L1.out",
   "follow_up": [
    "scripts/llm_t5_profile.py --replay 20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E6_rerank_L1",
   "exp": "E6",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t1_rerank",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--level",
    "L1",
    "--split",
    "dev",
    "--limit",
    "40",
    "--k",
    "30",
    "--max-tokens",
    "300"
   ],
   "rc": 0,
   "seconds": 177.5,
   "run_dir": "20261023_042523_t1_rerank_L1_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 40,
    "usage_records": 40,
    "prompt_tokens": 81366,
    "completion_tokens": 10672,
    "cost_usd": 0.2233,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 40,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 40
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E6_rerank_L1.out"
  },
  {
   "label": "E6_rerank_L5",
   "exp": "E6",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t1_rerank",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--level",
    "L5",
    "--split",
    "dev",
    "--limit",
    "40",
    "--k",
    "30",
    "--max-tokens",
    "300"
   ],
   "rc": 0,
   "seconds": 205.7,
   "run_dir": "20261023_042821_t1_rerank_L5_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 40,
    "usage_records": 40,
    "prompt_tokens": 49266,
    "completion_tokens": 9648,
    "cost_usd": 0.1581,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 40,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 40
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1-mini_E6_rerank_L5.out"
  }
 ],
 "finished": "2026-10-23T04:31:46+08:00"
}
== api_2026-10-22_xj-gpt-4.1_205353_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-22T20:53:53+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_110754_t0_closedbook_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112731_e10_agent_L3-H_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_114037_e10_agent_L1_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-22T20:53:53+08:00"
}
== api_2026-10-22_xj-gpt-4.1_214144_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-22T21:41:44+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "exp": "E5",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t0_closedbook",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 325.3,
   "run_dir": "20261022_214144_t0_closedbook_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 10950,
    "completion_tokens": 3470,
    "cost_usd": 0.2235,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1_E5_closedbook.out"
  },
  {
   "label": "E10_agent_L1_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 424.0,
   "run_dir": "20261022_214709_e10_agent_L1_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156708,
    "completion_tokens": 5185,
    "cost_usd": 1.597,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_214039.json",
    "2026-10-22_e10_shortlist_controls_20261022_214039.md",
    "2026-10-22_e10_shortlist_controls_20261022_214709.json",
    "2026-10-22_e10_shortlist_controls_20261022_214709.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L1_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_214709_e10_agent_L1_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_214709_e10_agent_L1_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3"
   ],
   "rc": 0,
   "seconds": 557.5,
   "run_dir": "20261022_215425_e10_agent_L3_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 142696,
    "completion_tokens": 4688,
    "cost_usd": 1.453,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_api_preflight.json",
    "2026-10-22_api_preflight.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_215404.json",
    "2026-10-22_e10_shortlist_controls_20261022_215404.md",
    "2026-10-22_e10_shortlist_controls_20261022_215425.json",
    "2026-10-22_e10_shortlist_controls_20261022_215425.md",
    "2026-10-22_e16_visual_L5_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L5_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v1.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L3_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_215425_e10_agent_L3_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_215425_e10_agent_L3_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3H_dev",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 480.9,
   "run_dir": "20261022_220353_e10_agent_L3-H_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 138786,
    "completion_tokens": 5576,
    "cost_usd": 1.4498,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_215936.json",
    "2026-10-22_e10_shortlist_controls_20261022_215936.md",
    "2026-10-22_e10_shortlist_controls_20261022_220353.json",
    "2026-10-22_e10_shortlist_controls_20261022_220353.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L3H_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_220353_e10_agent_L3-H_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_220353_e10_agent_L3-H_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 639.0,
   "run_dir": "20261022_221207_e10_agent_L5_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 96610,
    "completion_tokens": 4800,
    "cost_usd": 1.0423,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_214027.json",
    "2026-10-22_e10_shortlist_controls_20261022_214027.md",
    "2026-10-22_e10_shortlist_controls_20261022_220719.json",
    "2026-10-22_e10_shortlist_controls_20261022_220719.md",
    "2026-10-22_e10_shortlist_controls_20261022_221207.json",
    "2026-10-22_e10_shortlist_controls_20261022_221207.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L5_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_221207_e10_agent_L5_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_221207_e10_agent_L5_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 1317.0,
   "run_dir": "20261022_222258_e10_agent_L1_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 594852,
    "completion_tokens": 21937,
    "cost_usd": 6.0726,
    "cache_hits": 3,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 294
     }
    }
   },
   "reports": [
    "2026-10-22_commons_identity.json",
    "2026-10-22_commons_identity.md",
    "2026-10-22_commons_views.json",
    "2026-10-22_custody_events.json",
    "2026-10-22_custody_events.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L1_test_xj-claude-sonnet-4.6.json",
    "2026-10-22_e10_regate_L1_test_xj-claude-sonnet-4.6.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-pro.json",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-pro.md",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_212434.json",
    "2026-10-22_e10_shortlist_controls_20261022_212434.md",
    "2026-10-22_e10_shortlist_controls_20261022_213641.json",
    "2026-10-22_e10_shortlist_controls_20261022_213641.md",
    "2026-10-22_e10_shortlist_controls_20261022_220658.json",
    "2026-10-22_e10_shortlist_controls_20261022_220658.md",
    "2026-10-22_e10_shortlist_controls_20261022_221312.json",
    "2026-10-22_e10_shortlist_controls_20261022_221312.md",
    "2026-10-22_e10_shortlist_controls_20261022_221334.json",
    "2026-10-22_e10_shortlist_controls_20261022_221334.md",
    "2026-10-22_e10_shortlist_controls_20261022_222258.json",
    "2026-10-22_e10_shortlist_controls_20261022_222258.md",
    "2026-10-22_e10_shortlist_controls_20261022_222353.json",
    "2026-10-22_e10_shortlist_controls_20261022_222353.md",
    "2026-10-22_e10_shortlist_controls_20261022_222526.json",
    "2026-10-22_e10_shortlist_controls_20261022_222526.md",
    "2026-10-22_e10_shortlist_controls_20261022_223020.json",
    "2026-10-22_e10_shortlist_controls_20261022_223020.md",
    "2026-10-22_e10_shortlist_controls_20261022_223210.json",
    "2026-10-22_e10_shortlist_controls_20261022_223210.md",
    "2026-10-22_e10_shortlist_controls_20261022_223403.json",
    "2026-10-22_e10_shortlist_controls_20261022_223403.md",
    "2026-10-22_e10_shortlist_controls_20261022_224025.json",
    "2026-10-22_e10_shortlist_controls_20261022_224025.md",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_enrich_records.json",
    "2026-10-22_extra_views.json",
    "2026-10-22_fact_cards.json",
    "2026-10-22_fact_cards.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-claude-sonnet-4.6.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-claude-sonnet-4.6.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v2.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-pro.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-pro.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.md",
    "2026-10-22_media_integrity.json",
    "2026-10-22_media_integrity.md",
    "2026-10-22_media_usability.json",
    "2026-10-22_media_usability.md",
    "2026-10-22_membership_evidence.json",
    "2026-10-22_membership_evidence.md",
    "2026-10-22_near_duplicates.json",
    "2026-10-22_near_duplicates.md",
    "2026-10-22_nga_views.json",
    "2026-10-22_quality_audit.json",
    "2026-10-22_quality_audit.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md",
    "2026-10-22_shortlist_shortcuts.json",
    "2026-10-22_shortlist_shortcuts.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md",
    "2026-10-22_text_screen.json",
    "2026-10-22_text_screen.md",
    "2026-10-22_wikidata_deep.json",
    "2026-10-22_wikidata_deep.md",
    "2026-10-22_wikipedia_dump.json"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L1_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_222258_e10_agent_L1_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_222258_e10_agent_L1_xj-gpt-4.1 (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-22T22:45:42+08:00"
}
== api_2026-10-22_xj-gpt-4.1_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-22T21:41:44+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "exp": "E5",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t0_closedbook",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 325.3,
   "run_dir": "20261022_214144_t0_closedbook_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 10950,
    "completion_tokens": 3470,
    "cost_usd": 0.2235,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [],
   "output": "api_2026-10-22_xj-gpt-4.1_E5_closedbook.out"
  },
  {
   "label": "E10_agent_L1_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 424.0,
   "run_dir": "20261022_214709_e10_agent_L1_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156708,
    "completion_tokens": 5185,
    "cost_usd": 1.597,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_214039.json",
    "2026-10-22_e10_shortlist_controls_20261022_214039.md",
    "2026-10-22_e10_shortlist_controls_20261022_214709.json",
    "2026-10-22_e10_shortlist_controls_20261022_214709.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L1_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_214709_e10_agent_L1_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_214709_e10_agent_L1_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3"
   ],
   "rc": 0,
   "seconds": 557.5,
   "run_dir": "20261022_215425_e10_agent_L3_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 142696,
    "completion_tokens": 4688,
    "cost_usd": 1.453,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_api_preflight.json",
    "2026-10-22_api_preflight.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_215404.json",
    "2026-10-22_e10_shortlist_controls_20261022_215404.md",
    "2026-10-22_e10_shortlist_controls_20261022_215425.json",
    "2026-10-22_e10_shortlist_controls_20261022_215425.md",
    "2026-10-22_e16_visual_L5_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L5_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v1.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L3_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_215425_e10_agent_L3_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_215425_e10_agent_L3_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3H_dev",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 480.9,
   "run_dir": "20261022_220353_e10_agent_L3-H_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 138786,
    "completion_tokens": 5576,
    "cost_usd": 1.4498,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_215936.json",
    "2026-10-22_e10_shortlist_controls_20261022_215936.md",
    "2026-10-22_e10_shortlist_controls_20261022_220353.json",
    "2026-10-22_e10_shortlist_controls_20261022_220353.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L3H_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_220353_e10_agent_L3-H_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_220353_e10_agent_L3-H_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 639.0,
   "run_dir": "20261022_221207_e10_agent_L5_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 96610,
    "completion_tokens": 4800,
    "cost_usd": 1.0423,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_214027.json",
    "2026-10-22_e10_shortlist_controls_20261022_214027.md",
    "2026-10-22_e10_shortlist_controls_20261022_220719.json",
    "2026-10-22_e10_shortlist_controls_20261022_220719.md",
    "2026-10-22_e10_shortlist_controls_20261022_221207.json",
    "2026-10-22_e10_shortlist_controls_20261022_221207.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L5_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_221207_e10_agent_L5_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_221207_e10_agent_L5_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 1317.0,
   "run_dir": "20261022_222258_e10_agent_L1_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 594852,
    "completion_tokens": 21937,
    "cost_usd": 6.0726,
    "cache_hits": 3,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 294
     }
    }
   },
   "reports": [
    "2026-10-22_commons_identity.json",
    "2026-10-22_commons_identity.md",
    "2026-10-22_commons_views.json",
    "2026-10-22_custody_events.json",
    "2026-10-22_custody_events.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L1_test_xj-claude-sonnet-4.6.json",
    "2026-10-22_e10_regate_L1_test_xj-claude-sonnet-4.6.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-pro.json",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-pro.md",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_212434.json",
    "2026-10-22_e10_shortlist_controls_20261022_212434.md",
    "2026-10-22_e10_shortlist_controls_20261022_213641.json",
    "2026-10-22_e10_shortlist_controls_20261022_213641.md",
    "2026-10-22_e10_shortlist_controls_20261022_220658.json",
    "2026-10-22_e10_shortlist_controls_20261022_220658.md",
    "2026-10-22_e10_shortlist_controls_20261022_221312.json",
    "2026-10-22_e10_shortlist_controls_20261022_221312.md",
    "2026-10-22_e10_shortlist_controls_20261022_221334.json",
    "2026-10-22_e10_shortlist_controls_20261022_221334.md",
    "2026-10-22_e10_shortlist_controls_20261022_222258.json",
    "2026-10-22_e10_shortlist_controls_20261022_222258.md",
    "2026-10-22_e10_shortlist_controls_20261022_222353.json",
    "2026-10-22_e10_shortlist_controls_20261022_222353.md",
    "2026-10-22_e10_shortlist_controls_20261022_222526.json",
    "2026-10-22_e10_shortlist_controls_20261022_222526.md",
    "2026-10-22_e10_shortlist_controls_20261022_223020.json",
    "2026-10-22_e10_shortlist_controls_20261022_223020.md",
    "2026-10-22_e10_shortlist_controls_20261022_223210.json",
    "2026-10-22_e10_shortlist_controls_20261022_223210.md",
    "2026-10-22_e10_shortlist_controls_20261022_223403.json",
    "2026-10-22_e10_shortlist_controls_20261022_223403.md",
    "2026-10-22_e10_shortlist_controls_20261022_224025.json",
    "2026-10-22_e10_shortlist_controls_20261022_224025.md",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_enrich_records.json",
    "2026-10-22_extra_views.json",
    "2026-10-22_fact_cards.json",
    "2026-10-22_fact_cards.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-claude-sonnet-4.6.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-claude-sonnet-4.6.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v2.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-pro.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-pro.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.md",
    "2026-10-22_media_integrity.json",
    "2026-10-22_media_integrity.md",
    "2026-10-22_media_usability.json",
    "2026-10-22_media_usability.md",
    "2026-10-22_membership_evidence.json",
    "2026-10-22_membership_evidence.md",
    "2026-10-22_near_duplicates.json",
    "2026-10-22_near_duplicates.md",
    "2026-10-22_nga_views.json",
    "2026-10-22_quality_audit.json",
    "2026-10-22_quality_audit.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md",
    "2026-10-22_shortlist_shortcuts.json",
    "2026-10-22_shortlist_shortcuts.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md",
    "2026-10-22_text_screen.json",
    "2026-10-22_text_screen.md",
    "2026-10-22_wikidata_deep.json",
    "2026-10-22_wikidata_deep.md",
    "2026-10-22_wikipedia_dump.json"
   ],
   "output": "api_2026-10-22_xj-gpt-4.1_E10_agent_L1_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_222258_e10_agent_L1_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_222258_e10_agent_L1_xj-gpt-4.1 (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-22T22:45:42+08:00"
}
== api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-22T20:53:58+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "exp": "E5",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t0_closedbook",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 478.5,
   "run_dir": "20261022_205358_t0_closedbook_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 10870,
    "completion_tokens": 27449,
    "cost_usd": 0.5926,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L2-T_test_mimo-v2.6-flash.json",
    "2026-10-22_e10_regate_L2-T_test_mimo-v2.6-flash.md",
    "2026-10-22_e10_shortlist_controls_20261022_205058.json",
    "2026-10-22_e10_shortlist_controls_20261022_205058.md",
    "2026-10-22_llm_reunion_agent_L2-T_test_mimo-v2.6-flash.json",
    "2026-10-22_llm_reunion_agent_L2-T_test_mimo-v2.6-flash.md",
    "2026-10-22_oa_fulltext.json"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E5_closedbook.out"
  },
  {
   "label": "E10_agent_L1_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 535.9,
   "run_dir": "20261022_210157_e10_agent_L1_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156628,
    "completion_tokens": 38009,
    "cost_usd": 1.2991,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_commons_identity.json",
    "2026-10-22_commons_identity.md",
    "2026-10-22_e10_regate_L1_test_xj-qwen3.5-27b.json",
    "2026-10-22_e10_regate_L1_test_xj-qwen3.5-27b.md",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L2-T_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L2-T_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3-H_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L3-H_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3-H_xj-claude-sonnet-4.6.json",
    "2026-10-22_e10_regate_L3-H_xj-claude-sonnet-4.6.md",
    "2026-10-22_e10_shortlist_controls_20261022_203932.json",
    "2026-10-22_e10_shortlist_controls_20261022_203932.md",
    "2026-10-22_e10_shortlist_controls_20261022_205316.json",
    "2026-10-22_e10_shortlist_controls_20261022_205316.md",
    "2026-10-22_e10_shortlist_controls_20261022_210157.json",
    "2026-10-22_e10_shortlist_controls_20261022_210157.md",
    "2026-10-22_e10_shortlist_controls_20261022_210559.json",
    "2026-10-22_e10_shortlist_controls_20261022_210559.md",
    "2026-10-22_e10_shortlist_controls_20261022_210809.json",
    "2026-10-22_e10_shortlist_controls_20261022_210809.md",
    "2026-10-22_fact_cards.json",
    "2026-10-22_fact_cards.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-qwen3.5-27b.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-qwen3.5-27b.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_v1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L2-T_mimo-v2.6-pro.json",
    "2026-10-22_llm_reunion_agent_L2-T_mimo-v2.6-pro.md",
    "2026-10-22_llm_reunion_agent_L3-H_mimo-v2.6-pro.json",
    "2026-10-22_llm_reunion_agent_L3-H_mimo-v2.6-pro.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-claude-sonnet-4.6.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-claude-sonnet-4.6.md",
    "2026-10-22_media_usability.json",
    "2026-10-22_media_usability.md",
    "2026-10-22_membership_evidence.json",
    "2026-10-22_membership_evidence.md",
    "2026-10-22_near_duplicates.json",
    "2026-10-22_near_duplicates.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md",
    "2026-10-22_text_screen.json",
    "2026-10-22_text_screen.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L1_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3"
   ],
   "rc": 0,
   "seconds": 541.7,
   "run_dir": "20261022_211105_e10_agent_L3_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 142616,
    "completion_tokens": 49352,
    "cost_usd": 1.4814,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L2-T_test_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L2-T_test_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_211029.json",
    "2026-10-22_e10_shortlist_controls_20261022_211029.md",
    "2026-10-22_e10_shortlist_controls_20261022_211037.json",
    "2026-10-22_e10_shortlist_controls_20261022_211037.md",
    "2026-10-22_e10_shortlist_controls_20261022_211105.json",
    "2026-10-22_e10_shortlist_controls_20261022_211105.md",
    "2026-10-22_e10_shortlist_controls_20261022_211513.json",
    "2026-10-22_e10_shortlist_controls_20261022_211513.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_v2.md",
    "2026-10-22_llm_reunion_agent_L2-T_test_mimo-v2.6-pro.json",
    "2026-10-22_llm_reunion_agent_L2-T_test_mimo-v2.6-pro.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4-mini.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L3_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3H_dev",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 525.6,
   "run_dir": "20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 138706,
    "completion_tokens": 52792,
    "cost_usd": 1.5379,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L5_xj-claude-sonnet-4.6.json",
    "2026-10-22_e10_regate_L5_xj-claude-sonnet-4.6.md",
    "2026-10-22_e10_shortlist_controls_20261022_210947.json",
    "2026-10-22_e10_shortlist_controls_20261022_210947.md",
    "2026-10-22_e10_shortlist_controls_20261022_212019.json",
    "2026-10-22_e10_shortlist_controls_20261022_212019.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L5_xj-claude-sonnet-4.6.json",
    "2026-10-22_llm_reunion_agent_L5_xj-claude-sonnet-4.6.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L3H_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 658.5,
   "run_dir": "20261022_212916_e10_agent_L5_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 96530,
    "completion_tokens": 55532,
    "cost_usd": 1.4508,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.md",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-pro.json",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-pro.md",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_205129.json",
    "2026-10-22_e10_shortlist_controls_20261022_205129.md",
    "2026-10-22_e10_shortlist_controls_20261022_211710.json",
    "2026-10-22_e10_shortlist_controls_20261022_211710.md",
    "2026-10-22_e10_shortlist_controls_20261022_212916.json",
    "2026-10-22_e10_shortlist_controls_20261022_212916.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_v1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_v1.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_v2.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_v2.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-pro.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-pro.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4-mini.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L5_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 1933.8,
   "run_dir": "20261022_214027_e10_agent_L1_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 594558,
    "completion_tokens": 149743,
    "cost_usd": 4.9997,
    "cache_hits": 3,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 294
     }
    }
   },
   "reports": [
    "2026-10-22_api_preflight.json",
    "2026-10-22_api_preflight.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_213037.json",
    "2026-10-22_e10_shortlist_controls_20261022_213037.md",
    "2026-10-22_e10_shortlist_controls_20261022_214027.json",
    "2026-10-22_e10_shortlist_controls_20261022_214027.md",
    "2026-10-22_e10_shortlist_controls_20261022_214039.json",
    "2026-10-22_e10_shortlist_controls_20261022_214039.md",
    "2026-10-22_e10_shortlist_controls_20261022_214709.json",
    "2026-10-22_e10_shortlist_controls_20261022_214709.md",
    "2026-10-22_e10_shortlist_controls_20261022_215404.json",
    "2026-10-22_e10_shortlist_controls_20261022_215404.md",
    "2026-10-22_e10_shortlist_controls_20261022_215425.json",
    "2026-10-22_e10_shortlist_controls_20261022_215425.md",
    "2026-10-22_e10_shortlist_controls_20261022_215936.json",
    "2026-10-22_e10_shortlist_controls_20261022_215936.md",
    "2026-10-22_e10_shortlist_controls_20261022_220353.json",
    "2026-10-22_e10_shortlist_controls_20261022_220353.md",
    "2026-10-22_e10_shortlist_controls_20261022_220719.json",
    "2026-10-22_e10_shortlist_controls_20261022_220719.md",
    "2026-10-22_e16_visual_L5_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L5_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v1.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L1_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-22T22:13:32+08:00"
}
== api_2026-10-22_xj-gpt-5.4-mini_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-22T20:53:58+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "exp": "E5",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t0_closedbook",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 478.5,
   "run_dir": "20261022_205358_t0_closedbook_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 10870,
    "completion_tokens": 27449,
    "cost_usd": 0.5926,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L2-T_test_mimo-v2.6-flash.json",
    "2026-10-22_e10_regate_L2-T_test_mimo-v2.6-flash.md",
    "2026-10-22_e10_shortlist_controls_20261022_205058.json",
    "2026-10-22_e10_shortlist_controls_20261022_205058.md",
    "2026-10-22_llm_reunion_agent_L2-T_test_mimo-v2.6-flash.json",
    "2026-10-22_llm_reunion_agent_L2-T_test_mimo-v2.6-flash.md",
    "2026-10-22_oa_fulltext.json"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E5_closedbook.out"
  },
  {
   "label": "E10_agent_L1_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 535.9,
   "run_dir": "20261022_210157_e10_agent_L1_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156628,
    "completion_tokens": 38009,
    "cost_usd": 1.2991,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_commons_identity.json",
    "2026-10-22_commons_identity.md",
    "2026-10-22_e10_regate_L1_test_xj-qwen3.5-27b.json",
    "2026-10-22_e10_regate_L1_test_xj-qwen3.5-27b.md",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L2-T_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L2-T_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3-H_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L3-H_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3-H_xj-claude-sonnet-4.6.json",
    "2026-10-22_e10_regate_L3-H_xj-claude-sonnet-4.6.md",
    "2026-10-22_e10_shortlist_controls_20261022_203932.json",
    "2026-10-22_e10_shortlist_controls_20261022_203932.md",
    "2026-10-22_e10_shortlist_controls_20261022_205316.json",
    "2026-10-22_e10_shortlist_controls_20261022_205316.md",
    "2026-10-22_e10_shortlist_controls_20261022_210157.json",
    "2026-10-22_e10_shortlist_controls_20261022_210157.md",
    "2026-10-22_e10_shortlist_controls_20261022_210559.json",
    "2026-10-22_e10_shortlist_controls_20261022_210559.md",
    "2026-10-22_e10_shortlist_controls_20261022_210809.json",
    "2026-10-22_e10_shortlist_controls_20261022_210809.md",
    "2026-10-22_fact_cards.json",
    "2026-10-22_fact_cards.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-qwen3.5-27b.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-qwen3.5-27b.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_v1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L2-T_mimo-v2.6-pro.json",
    "2026-10-22_llm_reunion_agent_L2-T_mimo-v2.6-pro.md",
    "2026-10-22_llm_reunion_agent_L3-H_mimo-v2.6-pro.json",
    "2026-10-22_llm_reunion_agent_L3-H_mimo-v2.6-pro.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-claude-sonnet-4.6.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-claude-sonnet-4.6.md",
    "2026-10-22_media_usability.json",
    "2026-10-22_media_usability.md",
    "2026-10-22_membership_evidence.json",
    "2026-10-22_membership_evidence.md",
    "2026-10-22_near_duplicates.json",
    "2026-10-22_near_duplicates.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md",
    "2026-10-22_text_screen.json",
    "2026-10-22_text_screen.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L1_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3"
   ],
   "rc": 0,
   "seconds": 541.7,
   "run_dir": "20261022_211105_e10_agent_L3_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 142616,
    "completion_tokens": 49352,
    "cost_usd": 1.4814,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.json",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-flash.md",
    "2026-10-22_e10_regate_L2-T_test_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L2-T_test_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_211029.json",
    "2026-10-22_e10_shortlist_controls_20261022_211029.md",
    "2026-10-22_e10_shortlist_controls_20261022_211037.json",
    "2026-10-22_e10_shortlist_controls_20261022_211037.md",
    "2026-10-22_e10_shortlist_controls_20261022_211105.json",
    "2026-10-22_e10_shortlist_controls_20261022_211105.md",
    "2026-10-22_e10_shortlist_controls_20261022_211513.json",
    "2026-10-22_e10_shortlist_controls_20261022_211513.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-flash_v2.md",
    "2026-10-22_llm_reunion_agent_L2-T_test_mimo-v2.6-pro.json",
    "2026-10-22_llm_reunion_agent_L2-T_test_mimo-v2.6-pro.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4-mini.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L3_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3H_dev",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 525.6,
   "run_dir": "20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 138706,
    "completion_tokens": 52792,
    "cost_usd": 1.5379,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L5_xj-claude-sonnet-4.6.json",
    "2026-10-22_e10_regate_L5_xj-claude-sonnet-4.6.md",
    "2026-10-22_e10_shortlist_controls_20261022_210947.json",
    "2026-10-22_e10_shortlist_controls_20261022_210947.md",
    "2026-10-22_e10_shortlist_controls_20261022_212019.json",
    "2026-10-22_e10_shortlist_controls_20261022_212019.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L5_xj-claude-sonnet-4.6.json",
    "2026-10-22_llm_reunion_agent_L5_xj-claude-sonnet-4.6.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L3H_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 658.5,
   "run_dir": "20261022_212916_e10_agent_L5_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 96530,
    "completion_tokens": 55532,
    "cost_usd": 1.4508,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.md",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-pro.json",
    "2026-10-22_e10_regate_L1_xj-gemini-2.5-pro.md",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_205129.json",
    "2026-10-22_e10_shortlist_controls_20261022_205129.md",
    "2026-10-22_e10_shortlist_controls_20261022_211710.json",
    "2026-10-22_e10_shortlist_controls_20261022_211710.md",
    "2026-10-22_e10_shortlist_controls_20261022_212916.json",
    "2026-10-22_e10_shortlist_controls_20261022_212916.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_v1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_v1.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_v2.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_v2.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-pro.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gemini-2.5-pro.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4-mini.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L5_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 1933.8,
   "run_dir": "20261022_214027_e10_agent_L1_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 594558,
    "completion_tokens": 149743,
    "cost_usd": 4.9997,
    "cache_hits": 3,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 294
     }
    }
   },
   "reports": [
    "2026-10-22_api_preflight.json",
    "2026-10-22_api_preflight.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-flash.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_213037.json",
    "2026-10-22_e10_shortlist_controls_20261022_213037.md",
    "2026-10-22_e10_shortlist_controls_20261022_214027.json",
    "2026-10-22_e10_shortlist_controls_20261022_214027.md",
    "2026-10-22_e10_shortlist_controls_20261022_214039.json",
    "2026-10-22_e10_shortlist_controls_20261022_214039.md",
    "2026-10-22_e10_shortlist_controls_20261022_214709.json",
    "2026-10-22_e10_shortlist_controls_20261022_214709.md",
    "2026-10-22_e10_shortlist_controls_20261022_215404.json",
    "2026-10-22_e10_shortlist_controls_20261022_215404.md",
    "2026-10-22_e10_shortlist_controls_20261022_215425.json",
    "2026-10-22_e10_shortlist_controls_20261022_215425.md",
    "2026-10-22_e10_shortlist_controls_20261022_215936.json",
    "2026-10-22_e10_shortlist_controls_20261022_215936.md",
    "2026-10-22_e10_shortlist_controls_20261022_220353.json",
    "2026-10-22_e10_shortlist_controls_20261022_220353.md",
    "2026-10-22_e10_shortlist_controls_20261022_220719.json",
    "2026-10-22_e10_shortlist_controls_20261022_220719.md",
    "2026-10-22_e16_visual_L5_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L5_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-flash_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v1.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4-mini_E10_agent_L1_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-22T22:13:32+08:00"
}
== api_2026-10-22_xj-gpt-5.4_220008_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-22T22:00:08+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "exp": "E5",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t0_closedbook",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 430.6,
   "run_dir": "20261022_220008_t0_closedbook_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 10870,
    "completion_tokens": 4163,
    "cost_usd": 0.2868,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 61,
      "gpt-5.4": 19
     }
    }
   },
   "reports": [
    "2026-10-22_api_preflight.json",
    "2026-10-22_api_preflight.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_215425.json",
    "2026-10-22_e10_shortlist_controls_20261022_215425.md",
    "2026-10-22_e10_shortlist_controls_20261022_215936.json",
    "2026-10-22_e10_shortlist_controls_20261022_215936.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E5_closedbook.out"
  },
  {
   "label": "E10_agent_L1_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 339.3,
   "run_dir": "20261022_220719_e10_agent_L1_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156628,
    "completion_tokens": 6494,
    "cost_usd": 1.5647,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 59,
      "gpt-5.4": 21
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_220353.json",
    "2026-10-22_e10_shortlist_controls_20261022_220353.md",
    "2026-10-22_e10_shortlist_controls_20261022_220719.json",
    "2026-10-22_e10_shortlist_controls_20261022_220719.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L1_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_220719_e10_agent_L1_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_220719_e10_agent_L1_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3"
   ],
   "rc": 0,
   "seconds": 626.9,
   "run_dir": "20261022_221312_e10_agent_L3_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 142616,
    "completion_tokens": 5276,
    "cost_usd": 1.3942,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 57,
      "gpt-5.4": 23
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_214027.json",
    "2026-10-22_e10_shortlist_controls_20261022_214027.md",
    "2026-10-22_e10_shortlist_controls_20261022_221207.json",
    "2026-10-22_e10_shortlist_controls_20261022_221207.md",
    "2026-10-22_e10_shortlist_controls_20261022_221312.json",
    "2026-10-22_e10_shortlist_controls_20261022_221312.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L3_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_221312_e10_agent_L3_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_221312_e10_agent_L3_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3H_dev",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 359.1,
   "run_dir": "20261022_222353_e10_agent_L3-H_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 138706,
    "completion_tokens": 5407,
    "cost_usd": 1.3692,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 59,
      "gpt-5.4": 21
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_220658.json",
    "2026-10-22_e10_shortlist_controls_20261022_220658.md",
    "2026-10-22_e10_shortlist_controls_20261022_221334.json",
    "2026-10-22_e10_shortlist_controls_20261022_221334.md",
    "2026-10-22_e10_shortlist_controls_20261022_222353.json",
    "2026-10-22_e10_shortlist_controls_20261022_222353.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v1.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L3H_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_222353_e10_agent_L3-H_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_222353_e10_agent_L3-H_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 352.7,
   "run_dir": "20261022_223020_e10_agent_L5_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 96530,
    "completion_tokens": 5079,
    "cost_usd": 1.016,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 64,
      "gpt-5.4": 16
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-claude-sonnet-4.6.json",
    "2026-10-22_e10_regate_L1_test_xj-claude-sonnet-4.6.md",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-pro.json",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-pro.md",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_212434.json",
    "2026-10-22_e10_shortlist_controls_20261022_212434.md",
    "2026-10-22_e10_shortlist_controls_20261022_213641.json",
    "2026-10-22_e10_shortlist_controls_20261022_213641.md",
    "2026-10-22_e10_shortlist_controls_20261022_222526.json",
    "2026-10-22_e10_shortlist_controls_20261022_222526.md",
    "2026-10-22_e10_shortlist_controls_20261022_223020.json",
    "2026-10-22_e10_shortlist_controls_20261022_223020.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-claude-sonnet-4.6.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-claude-sonnet-4.6.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v2.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-pro.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-pro.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L5_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_223020_e10_agent_L5_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_223020_e10_agent_L5_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 1325.6,
   "run_dir": "20261022_223622_e10_agent_L1_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 594558,
    "completion_tokens": 25459,
    "cost_usd": 5.9108,
    "cache_hits": 3,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 221,
      "gpt-5.4": 73
     }
    }
   },
   "reports": [
    "2026-10-22_commons_identity.json",
    "2026-10-22_commons_identity.md",
    "2026-10-22_commons_views.json",
    "2026-10-22_custody_events.json",
    "2026-10-22_custody_events.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_222258.json",
    "2026-10-22_e10_shortlist_controls_20261022_222258.md",
    "2026-10-22_e10_shortlist_controls_20261022_223210.json",
    "2026-10-22_e10_shortlist_controls_20261022_223210.md",
    "2026-10-22_e10_shortlist_controls_20261022_223403.json",
    "2026-10-22_e10_shortlist_controls_20261022_223403.md",
    "2026-10-22_e10_shortlist_controls_20261022_223622.json",
    "2026-10-22_e10_shortlist_controls_20261022_223622.md",
    "2026-10-22_e10_shortlist_controls_20261022_224025.json",
    "2026-10-22_e10_shortlist_controls_20261022_224025.md",
    "2026-10-22_e10_shortlist_controls_20261022_224522.json",
    "2026-10-22_e10_shortlist_controls_20261022_224522.md",
    "2026-10-22_e16_visual_L1_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L1_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_enrich_records.json",
    "2026-10-22_extra_views.json",
    "2026-10-22_fact_cards.json",
    "2026-10-22_fact_cards.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.md",
    "2026-10-22_media_integrity.json",
    "2026-10-22_media_integrity.md",
    "2026-10-22_media_usability.json",
    "2026-10-22_media_usability.md",
    "2026-10-22_membership_evidence.json",
    "2026-10-22_membership_evidence.md",
    "2026-10-22_near_duplicates.json",
    "2026-10-22_near_duplicates.md",
    "2026-10-22_nga_views.json",
    "2026-10-22_oa_fulltext.json",
    "2026-10-22_quality_audit.json",
    "2026-10-22_quality_audit.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md",
    "2026-10-22_shortlist_shortcuts.json",
    "2026-10-22_shortlist_shortcuts.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md",
    "2026-10-22_text_screen.json",
    "2026-10-22_text_screen.md",
    "2026-10-22_wikidata_deep.json",
    "2026-10-22_wikidata_deep.md",
    "2026-10-22_wikipedia_dump.json"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L1_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_223622_e10_agent_L1_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_223622_e10_agent_L1_xj-gpt-5.4 (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-22T22:59:14+08:00"
}
== api_2026-10-22_xj-gpt-5.4_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-22T22:00:08+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "exp": "E5",
   "argv": [
    "scripts/llm_eval_harness.py",
    "--task",
    "t0_closedbook",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0"
   ],
   "rc": 0,
   "seconds": 430.6,
   "run_dir": "20261022_220008_t0_closedbook_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 10870,
    "completion_tokens": 4163,
    "cost_usd": 0.2868,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 61,
      "gpt-5.4": 19
     }
    }
   },
   "reports": [
    "2026-10-22_api_preflight.json",
    "2026-10-22_api_preflight.md",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_215425.json",
    "2026-10-22_e10_shortlist_controls_20261022_215425.md",
    "2026-10-22_e10_shortlist_controls_20261022_215936.json",
    "2026-10-22_e10_shortlist_controls_20261022_215936.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_v2.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E5_closedbook.out"
  },
  {
   "label": "E10_agent_L1_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 339.3,
   "run_dir": "20261022_220719_e10_agent_L1_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 156628,
    "completion_tokens": 6494,
    "cost_usd": 1.5647,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 59,
      "gpt-5.4": 21
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_220353.json",
    "2026-10-22_e10_shortlist_controls_20261022_220353.md",
    "2026-10-22_e10_shortlist_controls_20261022_220719.json",
    "2026-10-22_e10_shortlist_controls_20261022_220719.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L1_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_220719_e10_agent_L1_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_220719_e10_agent_L1_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3"
   ],
   "rc": 0,
   "seconds": 626.9,
   "run_dir": "20261022_221312_e10_agent_L3_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 142616,
    "completion_tokens": 5276,
    "cost_usd": 1.3942,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 57,
      "gpt-5.4": 23
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L3_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L5_xj-gpt-4.1.md",
    "2026-10-22_e10_shortlist_controls_20261022_214027.json",
    "2026-10-22_e10_shortlist_controls_20261022_214027.md",
    "2026-10-22_e10_shortlist_controls_20261022_221207.json",
    "2026-10-22_e10_shortlist_controls_20261022_221207.md",
    "2026-10-22_e10_shortlist_controls_20261022_221312.json",
    "2026-10-22_e10_shortlist_controls_20261022_221312.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L3_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_221312_e10_agent_L3_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_221312_e10_agent_L3_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3H_dev",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 359.1,
   "run_dir": "20261022_222353_e10_agent_L3-H_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 138706,
    "completion_tokens": 5407,
    "cost_usd": 1.3692,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 59,
      "gpt-5.4": 21
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.json",
    "2026-10-22_e10_regate_L1_mimo-v2.6-pro.md",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L3-H_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_220658.json",
    "2026-10-22_e10_shortlist_controls_20261022_220658.md",
    "2026-10-22_e10_shortlist_controls_20261022_221334.json",
    "2026-10-22_e10_shortlist_controls_20261022_221334.md",
    "2026-10-22_e10_shortlist_controls_20261022_222353.json",
    "2026-10-22_e10_shortlist_controls_20261022_222353.md",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_mimo-v2.6-pro_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v1.md",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L3-H_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L3H_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_222353_e10_agent_L3-H_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_222353_e10_agent_L3-H_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 352.7,
   "run_dir": "20261022_223020_e10_agent_L5_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 96530,
    "completion_tokens": 5079,
    "cost_usd": 1.016,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 64,
      "gpt-5.4": 16
     }
    }
   },
   "reports": [
    "2026-10-22_e10_regate_L1_test_xj-claude-sonnet-4.6.json",
    "2026-10-22_e10_regate_L1_test_xj-claude-sonnet-4.6.md",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-pro.json",
    "2026-10-22_e10_regate_L3_xj-gemini-2.5-pro.md",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L5_xj-gpt-5.4.md",
    "2026-10-22_e10_shortlist_controls_20261022_212434.json",
    "2026-10-22_e10_shortlist_controls_20261022_212434.md",
    "2026-10-22_e10_shortlist_controls_20261022_213641.json",
    "2026-10-22_e10_shortlist_controls_20261022_213641.md",
    "2026-10-22_e10_shortlist_controls_20261022_222526.json",
    "2026-10-22_e10_shortlist_controls_20261022_222526.md",
    "2026-10-22_e10_shortlist_controls_20261022_223020.json",
    "2026-10-22_e10_shortlist_controls_20261022_223020.md",
    "2026-10-22_literature_enrich.json",
    "2026-10-22_literature_enrich.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-claude-sonnet-4.6.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-claude-sonnet-4.6.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_v2.md",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-pro.json",
    "2026-10-22_llm_reunion_agent_L3_xj-gemini-2.5-pro.md",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L5_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L5_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_223020_e10_agent_L5_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_223020_e10_agent_L5_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L1_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1"
   ],
   "rc": 0,
   "seconds": 1325.6,
   "run_dir": "20261022_223622_e10_agent_L1_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 594558,
    "completion_tokens": 25459,
    "cost_usd": 5.9108,
    "cache_hits": 3,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 221,
      "gpt-5.4": 73
     }
    }
   },
   "reports": [
    "2026-10-22_commons_identity.json",
    "2026-10-22_commons_identity.md",
    "2026-10-22_commons_views.json",
    "2026-10-22_custody_events.json",
    "2026-10-22_custody_events.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-4.1.md",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4.json",
    "2026-10-22_e10_regate_L1_test_xj-gpt-5.4.md",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.json",
    "2026-10-22_e10_regate_L1_xj-claude-haiku-4.5.md",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.json",
    "2026-10-22_e10_regate_L1_xj-gpt-4.1-mini.md",
    "2026-10-22_e10_shortlist_controls_20261022_222258.json",
    "2026-10-22_e10_shortlist_controls_20261022_222258.md",
    "2026-10-22_e10_shortlist_controls_20261022_223210.json",
    "2026-10-22_e10_shortlist_controls_20261022_223210.md",
    "2026-10-22_e10_shortlist_controls_20261022_223403.json",
    "2026-10-22_e10_shortlist_controls_20261022_223403.md",
    "2026-10-22_e10_shortlist_controls_20261022_223622.json",
    "2026-10-22_e10_shortlist_controls_20261022_223622.md",
    "2026-10-22_e10_shortlist_controls_20261022_224025.json",
    "2026-10-22_e10_shortlist_controls_20261022_224025.md",
    "2026-10-22_e10_shortlist_controls_20261022_224522.json",
    "2026-10-22_e10_shortlist_controls_20261022_224522.md",
    "2026-10-22_e16_visual_L1_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L1_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.json",
    "2026-10-22_e16_visual_L3_dev_xj-gemini-2.5-flash.md",
    "2026-10-22_enrich_records.json",
    "2026-10-22_extra_views.json",
    "2026-10-22_fact_cards.json",
    "2026-10-22_fact_cards.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-4.1.md",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4.json",
    "2026-10-22_llm_reunion_agent_L1_test_xj-gpt-5.4.md",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-claude-haiku-4.5_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_rep1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_rep1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v1.md",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.json",
    "2026-10-22_llm_reunion_agent_L1_xj-gpt-4.1-mini_v2.md",
    "2026-10-22_media_integrity.json",
    "2026-10-22_media_integrity.md",
    "2026-10-22_media_usability.json",
    "2026-10-22_media_usability.md",
    "2026-10-22_membership_evidence.json",
    "2026-10-22_membership_evidence.md",
    "2026-10-22_near_duplicates.json",
    "2026-10-22_near_duplicates.md",
    "2026-10-22_nga_views.json",
    "2026-10-22_oa_fulltext.json",
    "2026-10-22_quality_audit.json",
    "2026-10-22_quality_audit.md",
    "2026-10-22_release_validation.json",
    "2026-10-22_release_validation.md",
    "2026-10-22_shortlist_shortcuts.json",
    "2026-10-22_shortlist_shortcuts.md",
    "2026-10-22_temporal_ladder.json",
    "2026-10-22_temporal_ladder.md",
    "2026-10-22_text_screen.json",
    "2026-10-22_text_screen.md",
    "2026-10-22_wikidata_deep.json",
    "2026-10-22_wikidata_deep.md",
    "2026-10-22_wikipedia_dump.json"
   ],
   "output": "api_2026-10-22_xj-gpt-5.4_E10_agent_L1_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261022_223622_e10_agent_L1_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261022_223622_e10_agent_L1_xj-gpt-5.4 (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-22T22:59:14+08:00"
}
== api_2026-10-23_xj-gpt-4.1-mini_235009_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-23T23:50:09+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_110754_t0_closedbook_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112731_e10_agent_L3-H_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_114037_e10_agent_L1_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-23T23:50:09+08:00"
}
== api_2026-10-23_xj-gpt-4.1-mini_235024_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-23T23:50:24+08:00",
 "jobs": [
  {
   "label": "E10_agent_L1_dev_v1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1"
  },
  {
   "label": "E10_agent_L1_dev_v2",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2"
  },
  {
   "label": "E10_agent_L1_dev_rep1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1"
  },
  {
   "label": "E16_visual_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_225050_e16_visual_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_230933_e16_visual_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_232828_e16_visual_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator"
  },
  {
   "label": "E15_harness_L1_dev40",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_002216_harness_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E7_pair_verify_balanced",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_003611_c4_pair_verify_xj-gpt-4.1-mini"
  },
  {
   "label": "E10e_pointwise_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10c_visual_score",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_032614_e10c_visual_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E15_harness_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034446_harness_L2T_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_L1_both_orders",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4"
  },
  {
   "label": "E9_T5_profile_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042523_t1_rerank_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L5",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042821_t1_rerank_L5_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-23T23:50:24+08:00"
}
== api_2026-10-23_xj-gpt-4.1-mini_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-23T23:50:24+08:00",
 "jobs": [
  {
   "label": "E10_agent_L1_dev_v1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1"
  },
  {
   "label": "E10_agent_L1_dev_v2",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2"
  },
  {
   "label": "E10_agent_L1_dev_rep1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1"
  },
  {
   "label": "E16_visual_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_225050_e16_visual_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_230933_e16_visual_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_232828_e16_visual_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator"
  },
  {
   "label": "E15_harness_L1_dev40",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_002216_harness_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E7_pair_verify_balanced",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_003611_c4_pair_verify_xj-gpt-4.1-mini"
  },
  {
   "label": "E10e_pointwise_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10c_visual_score",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_032614_e10c_visual_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E15_harness_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034446_harness_L2T_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_L1_both_orders",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4"
  },
  {
   "label": "E9_T5_profile_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042523_t1_rerank_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L5",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042821_t1_rerank_L5_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-23T23:50:24+08:00"
}
== api_2026-10-23_xj-gpt-4.1_235019_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-23T23:50:19+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214144_t0_closedbook_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214709_e10_agent_L1_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_215425_e10_agent_L3_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_220353_e10_agent_L3-H_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_221207_e10_agent_L5_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_222258_e10_agent_L1_xj-gpt-4.1"
  }
 ],
 "finished": "2026-10-23T23:50:19+08:00"
}
== api_2026-10-23_xj-gpt-4.1_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-23T23:50:19+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214144_t0_closedbook_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214709_e10_agent_L1_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_215425_e10_agent_L3_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_220353_e10_agent_L3-H_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_221207_e10_agent_L5_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_222258_e10_agent_L1_xj-gpt-4.1"
  }
 ],
 "finished": "2026-10-23T23:50:19+08:00"
}
== api_2026-10-23_xj-gpt-5.4-mini_020546_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-23T02:05:46+08:00",
 "jobs": [
  {
   "label": "E10v2_L1_dev",
   "exp": "E10V2",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1",
    "--inputs",
    "v2"
   ],
   "rc": 0,
   "seconds": 506.4,
   "run_dir": "20261023_020549_e10_agent_L1_xj-gpt-5.4-mini_inV2",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 271278,
    "completion_tokens": 35242,
    "cost_usd": 1.6306,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-23_e10_regate_L1_xj-gpt-5.4-mini.json",
    "2026-10-23_e10_regate_L1_xj-gpt-5.4-mini.md",
    "2026-10-23_e10_shortlist_controls_20261023_020549.json",
    "2026-10-23_e10_shortlist_controls_20261023_020549.md",
    "2026-10-23_llm_reunion_agent_L1_xj-gpt-5.4-mini_inV2.json",
    "2026-10-23_llm_reunion_agent_L1_xj-gpt-5.4-mini_inV2.md",
    "2026-10-23_subset_report.json",
    "2026-10-23_subset_report.md"
   ],
   "output": "api_2026-10-23_xj-gpt-5.4-mini_E10v2_L1_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261023_020549_e10_agent_L1_xj-gpt-5.4-mini_inV2 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261023_020549_e10_agent_L1_xj-gpt-5.4-mini_inV2 (rc=0)"
   ]
  },
  {
   "label": "E10v2_L5_dev",
   "exp": "E10V2",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5",
    "--inputs",
    "v2"
   ],
   "rc": 0,
   "seconds": 594.6,
   "run_dir": "20261023_021530_e10_agent_L5_xj-gpt-5.4-mini_inV2",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 112008,
    "completion_tokens": 46538,
    "cost_usd": 1.321,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 80
     }
    }
   },
   "reports": [
    "2026-10-23_e10_regate_L5_xj-gpt-5.4-mini.json",
    "2026-10-23_e10_regate_L5_xj-gpt-5.4-mini.md",
    "2026-10-23_e10_shortlist_controls_20261023_021530.json",
    "2026-10-23_e10_shortlist_controls_20261023_021530.md",
    "2026-10-23_llm_reunion_agent_L5_xj-gpt-5.4-mini_inV2.json",
    "2026-10-23_llm_reunion_agent_L5_xj-gpt-5.4-mini_inV2.md",
    "2026-10-23_mllm_pair_verify_strata_xj-claude-haiku-4.5.json",
    "2026-10-23_mllm_pair_verify_strata_xj-claude-haiku-4.5.md",
    "2026-10-23_mllm_pair_verify_xj-claude-haiku-4.5.json",
    "2026-10-23_mllm_pair_verify_xj-claude-haiku-4.5.md"
   ],
   "output": "api_2026-10-23_xj-gpt-5.4-mini_E10v2_L5_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261023_021530_e10_agent_L5_xj-gpt-5.4-mini_inV2 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261023_021530_e10_agent_L5_xj-gpt-5.4-mini_inV2 (rc=0)"
   ]
  },
  {
   "label": "E10v2_L1_test",
   "exp": "E10V2T",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L1",
    "--inputs",
    "v2"
   ],
   "rc": 0,
   "seconds": 1800.3,
   "run_dir": "20261023_022638_e10_agent_L1_xj-gpt-5.4-mini_inV2",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 1031506,
    "completion_tokens": 136175,
    "cost_usd": 6.1594,
    "cache_hits": 4,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 294
     }
    }
   },
   "reports": [
    "2026-10-23_commons_identity.json",
    "2026-10-23_commons_identity.md",
    "2026-10-23_commons_views.json",
    "2026-10-23_custody_events.json",
    "2026-10-23_custody_events.md",
    "2026-10-23_e10_regate_L1_mimo-v2.6-flash.json",
    "2026-10-23_e10_regate_L1_mimo-v2.6-flash.md",
    "2026-10-23_e10_regate_L1_test_xj-gpt-5.4-mini.json",
    "2026-10-23_e10_regate_L1_test_xj-gpt-5.4-mini.md",
    "2026-10-23_e10_regate_L1_xj-gemini-2.5-flash.json",
    "2026-10-23_e10_regate_L1_xj-gemini-2.5-flash.md",
    "2026-10-23_e10_regate_L1_xj-gemini-3-pro.json",
    "2026-10-23_e10_regate_L1_xj-gemini-3-pro.md",
    "2026-10-23_e10_regate_L5_mimo-v2.6-flash-thinking.json",
    "2026-10-23_e10_regate_L5_mimo-v2.6-flash-thinking.md",
    "2026-10-23_e10_regate_L5_mimo-v2.6-flash.json",
    "2026-10-23_e10_regate_L5_mimo-v2.6-flash.md",
    "2026-10-23_e10_regate_L5_xj-gemini-2.5-flash.json",
    "2026-10-23_e10_regate_L5_xj-gemini-2.5-flash.md",
    "2026-10-23_e10_shortlist_controls_20261023_011435.json",
    "2026-10-23_e10_shortlist_controls_20261023_011435.md",
    "2026-10-23_e10_shortlist_controls_20261023_014442.json",
    "2026-10-23_e10_shortlist_controls_20261023_014442.md",
    "2026-10-23_e10_shortlist_controls_20261023_020549.json",
    "2026-10-23_e10_shortlist_controls_20261023_020549.md",
    "2026-10-23_e10_shortlist_controls_20261023_022638.json",
    "2026-10-23_e10_shortlist_controls_20261023_022638.md",
    "2026-10-23_e10_shortlist_controls_20261023_023027.json",
    "2026-10-23_e10_shortlist_controls_20261023_023027.md",
    "2026-10-23_e10_shortlist_controls_20261023_023824.json",
    "2026-10-23_e10_shortlist_controls_20261023_023824.md",
    "2026-10-23_e10_shortlist_controls_20261023_024757.json",
    "2026-10-23_e10_shortlist_controls_20261023_024757.md",
    "2026-10-23_e12m_model_verify.json",
    "2026-10-23_e12m_model_verify.md",
    "2026-10-23_enrich_records.json",
    "2026-10-23_extra_views.json",
    "2026-10-23_fact_cards.json",
    "2026-10-23_fact_cards.md",
    "2026-10-23_literature_enrich.json",
    "2026-10-23_literature_enrich.md",
    "2026-10-23_llm_reunion_agent_L1_mimo-v2.6-flash_inV2.json",
    "2026-10-23_llm_reunion_agent_L1_mimo-v2.6-flash_inV2.md",
    "2026-10-23_llm_reunion_agent_L1_test_xj-gpt-5.4-mini_inV2.json",
    "2026-10-23_llm_reunion_agent_L1_test_xj-gpt-5.4-mini_inV2.md",
    "2026-10-23_llm_reunion_agent_L1_xj-gemini-2.5-flash_inV2.json",
    "2026-10-23_llm_reunion_agent_L1_xj-gemini-2.5-flash_inV2.md",
    "2026-10-23_llm_reunion_agent_L1_xj-gemini-3-pro.json",
    "2026-10-23_llm_reunion_agent_L1_xj-gemini-3-pro.md",
    "2026-10-23_llm_reunion_agent_L5_mimo-v2.6-flash-thinking.json",
    "2026-10-23_llm_reunion_agent_L5_mimo-v2.6-flash-thinking.md",
    "2026-10-23_llm_reunion_agent_L5_mimo-v2.6-flash_inV2.json",
    "2026-10-23_llm_reunion_agent_L5_mimo-v2.6-flash_inV2.md",
    "2026-10-23_llm_reunion_agent_L5_xj-gemini-2.5-flash_inV2.json",
    "2026-10-23_llm_reunion_agent_L5_xj-gemini-2.5-flash_inV2.md",
    "2026-10-23_media_integrity.json",
    "2026-10-23_media_integrity.md",
    "2026-10-23_media_usability.json",
    "2026-10-23_media_usability.md",
    "2026-10-23_membership_evidence.json",
    "2026-10-23_membership_evidence.md",
    "2026-10-23_near_duplicates.json",
    "2026-10-23_near_duplicates.md",
    "2026-10-23_nga_views.json",
    "2026-10-23_oa_fulltext.json",
    "2026-10-23_quality_audit.json",
    "2026-10-23_quality_audit.md",
    "2026-10-23_release_validation.json",
    "2026-10-23_release_validation.md",
    "2026-10-23_shortlist_shortcuts.json",
    "2026-10-23_shortlist_shortcuts.md",
    "2026-10-23_temporal_ladder.json",
    "2026-10-23_temporal_ladder.md",
    "2026-10-23_text_screen.json",
    "2026-10-23_text_screen.md",
    "2026-10-23_v2_inputs_compare.json",
    "2026-10-23_v2_inputs_compare.md",
    "2026-10-23_wikidata_deep.json",
    "2026-10-23_wikidata_deep.md",
    "2026-10-23_wikipedia_dump.json"
   ],
   "output": "api_2026-10-23_xj-gpt-5.4-mini_E10v2_L1_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261023_022638_e10_agent_L1_xj-gpt-5.4-mini_inV2 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261023_022638_e10_agent_L1_xj-gpt-5.4-mini_inV2 (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-23T03:00:07+08:00"
}
== api_2026-10-23_xj-gpt-5.4-mini_235019_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-23T23:50:19+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_205358_t0_closedbook_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini"
  }
 ],
 "finished": "2026-10-23T23:50:19+08:00"
}
== api_2026-10-23_xj-gpt-5.4-mini_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-23T23:50:19+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_205358_t0_closedbook_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini"
  }
 ],
 "finished": "2026-10-23T23:50:19+08:00"
}
== api_2026-10-24_xj-gpt-4.1-mini_113934_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-24T11:39:34+08:00",
 "jobs": [
  {
   "label": "E10_agent_L2Ttitle_dev",
   "exp": "E10T",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 112.7,
   "run_dir": "20261024_113936_e10_agent_L2-T_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 32,
    "usage_records": 32,
    "prompt_tokens": 74112,
    "completion_tokens": 2415,
    "cost_usd": 0.1508,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 32,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 32
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L2-T_xj-gpt-4.1-mini.json",
    "2026-10-24_e10_regate_L2-T_xj-gpt-4.1-mini.md",
    "2026-10-24_e10_shortlist_controls_20261024_113936_e10_agent_L2-T_xj-gpt-4.1-mini.json",
    "2026-10-24_e10_shortlist_controls_20261024_113936_e10_agent_L2-T_xj-gpt-4.1-mini.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gpt-4.1-mini.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gpt-4.1-mini.md",
    "2026-10-24_scale_behavior_L1_test.json",
    "2026-10-24_scale_behavior_L1_test.md"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1-mini_E10_agent_L2Ttitle_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_113936_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_113936_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L2Ttitle_test",
   "exp": "E10T",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 355.0,
   "run_dir": "20261024_114133_e10_agent_L2-T_xj-gpt-4.1-mini",
   "run_json": true,
   "stats": {
    "calls": 91,
    "usage_records": 91,
    "prompt_tokens": 224902,
    "completion_tokens": 6753,
    "cost_usd": 0.4359,
    "cache_hits": 3,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1-mini",
     "with_model_returned": 91,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-mini-2025-04-14": 91
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L2-T_test_xj-gpt-4.1-mini.json",
    "2026-10-24_e10_regate_L2-T_test_xj-gpt-4.1-mini.md",
    "2026-10-24_e10_regate_L2-T_xj-claude-haiku-4.5.json",
    "2026-10-24_e10_regate_L2-T_xj-claude-haiku-4.5.md",
    "2026-10-24_e10_regate_L2-T_xj-gemini-2.5-flash.json",
    "2026-10-24_e10_regate_L2-T_xj-gemini-2.5-flash.md",
    "2026-10-24_e10_regate_L2-T_xj-qwen3.5-397b.json",
    "2026-10-24_e10_regate_L2-T_xj-qwen3.5-397b.md",
    "2026-10-24_e10_shortlist_controls_20261024_113936_e10_agent_L2-T_xj-claude-haiku-4.5.json",
    "2026-10-24_e10_shortlist_controls_20261024_113936_e10_agent_L2-T_xj-claude-haiku-4.5.md",
    "2026-10-24_e10_shortlist_controls_20261024_113936_e10_agent_L2-T_xj-gemini-2.5-flash.json",
    "2026-10-24_e10_shortlist_controls_20261024_113936_e10_agent_L2-T_xj-gemini-2.5-flash.md",
    "2026-10-24_e10_shortlist_controls_20261024_113936_e10_agent_L2-T_xj-qwen3.5-397b.json",
    "2026-10-24_e10_shortlist_controls_20261024_113936_e10_agent_L2-T_xj-qwen3.5-397b.md",
    "2026-10-24_e10_shortlist_controls_20261024_114133_e10_agent_L2-T_xj-gpt-4.1-mini.json",
    "2026-10-24_e10_shortlist_controls_20261024_114133_e10_agent_L2-T_xj-gpt-4.1-mini.md",
    "2026-10-24_literature_enrich.json",
    "2026-10-24_literature_enrich.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gpt-4.1-mini.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gpt-4.1-mini.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-claude-haiku-4.5.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-claude-haiku-4.5.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gemini-2.5-flash.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gemini-2.5-flash.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-qwen3.5-397b.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-qwen3.5-397b.md",
    "2026-10-24_preselector_ablation.json",
    "2026-10-24_preselector_ablation.md",
    "2026-10-24_supervised_control_L1_test.json",
    "2026-10-24_supervised_control_L1_test.md",
    "2026-10-24_supervised_control_L3-H_test.json",
    "2026-10-24_supervised_control_L3-H_test.md",
    "2026-10-24_supervised_control_L5_test.json",
    "2026-10-24_supervised_control_L5_test.md"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1-mini_E10_agent_L2Ttitle_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_114133_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_114133_e10_agent_L2-T_xj-gpt-4.1-mini (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-24T11:47:41+08:00"
}
== api_2026-10-24_xj-gpt-4.1-mini_130731_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-24T13:07:31+08:00",
 "jobs": [
  {
   "label": "E10_agent_L2Ttitle_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-4.1-mini_113934_suite.json -> 20261024_113936_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2Ttitle_test",
   "skipped": "done: api_2026-10-24_xj-gpt-4.1-mini_113934_suite.json -> 20261024_114133_e10_agent_L2-T_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-24T13:07:32+08:00"
}
== api_2026-10-24_xj-gpt-4.1-mini_201305_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-24T20:13:05+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_110754_t0_closedbook_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112731_e10_agent_L3-H_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_114037_e10_agent_L1_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-24T20:13:05+08:00"
}
== api_2026-10-24_xj-gpt-4.1-mini_201320_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-24T20:13:20+08:00",
 "jobs": [
  {
   "label": "E10_agent_L1_dev_v1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1"
  },
  {
   "label": "E10_agent_L1_dev_v2",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2"
  },
  {
   "label": "E10_agent_L1_dev_rep1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1"
  },
  {
   "label": "E16_visual_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_225050_e16_visual_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_230933_e16_visual_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_232828_e16_visual_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator"
  },
  {
   "label": "E15_harness_L1_dev40",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_002216_harness_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E7_pair_verify_balanced",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_003611_c4_pair_verify_xj-gpt-4.1-mini"
  },
  {
   "label": "E10e_pointwise_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10c_visual_score",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_032614_e10c_visual_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E15_harness_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034446_harness_L2T_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_L1_both_orders",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4"
  },
  {
   "label": "E9_T5_profile_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042523_t1_rerank_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L5",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042821_t1_rerank_L5_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-24T20:13:20+08:00"
}
== api_2026-10-24_xj-gpt-4.1-mini_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-24T20:13:20+08:00",
 "jobs": [
  {
   "label": "E10_agent_L1_dev_v1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1"
  },
  {
   "label": "E10_agent_L1_dev_v2",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2"
  },
  {
   "label": "E10_agent_L1_dev_rep1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1"
  },
  {
   "label": "E16_visual_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_225050_e16_visual_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_230933_e16_visual_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_232828_e16_visual_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator"
  },
  {
   "label": "E15_harness_L1_dev40",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_002216_harness_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E7_pair_verify_balanced",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_003611_c4_pair_verify_xj-gpt-4.1-mini"
  },
  {
   "label": "E10e_pointwise_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10c_visual_score",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_032614_e10c_visual_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E15_harness_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034446_harness_L2T_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_L1_both_orders",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4"
  },
  {
   "label": "E9_T5_profile_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042523_t1_rerank_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L5",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042821_t1_rerank_L5_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-24T20:13:20+08:00"
}
== api_2026-10-24_xj-gpt-4.1_040507_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-24T04:05:07+08:00",
 "jobs": [
  {
   "label": "E16_visual_L5_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--from-run",
    "20261013_233240_e10_agent_L5_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 1361.1,
   "run_dir": "20261024_040531_e16_visual_L5_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 485085,
    "completion_tokens": 9367,
    "cost_usd": 4.703,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L3-H_test_mimo-v2.6-flash.json",
    "2026-10-24_e10_regate_L3-H_test_mimo-v2.6-flash.md",
    "2026-10-24_e10_shortlist_controls_20261024_005009_e10_agent_L3-H_xj-gemini-3-pro.json",
    "2026-10-24_e10_shortlist_controls_20261024_005009_e10_agent_L3-H_xj-gemini-3-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_014837_e10_agent_L5_xj-claude-opus-4.6.json",
    "2026-10-24_e10_shortlist_controls_20261024_014837_e10_agent_L5_xj-claude-opus-4.6.md",
    "2026-10-24_e10_shortlist_controls_20261024_034615_e10_agent_L3-H_mimo-v2.6-flash.json",
    "2026-10-24_e10_shortlist_controls_20261024_034615_e10_agent_L3-H_mimo-v2.6-flash.md",
    "2026-10-24_e10e_pointwise_L1_xj-qwen3.5-122b.json",
    "2026-10-24_e10e_pointwise_L1_xj-qwen3.5-122b.md",
    "2026-10-24_e16_visual_L5_dev_xj-gpt-4.1.json",
    "2026-10-24_e16_visual_L5_dev_xj-gpt-4.1.md",
    "2026-10-24_llm_reunion_agent_L3-H_test_mimo-v2.6-flash.json",
    "2026-10-24_llm_reunion_agent_L3-H_test_mimo-v2.6-flash.md"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1_E16_visual_L5_dev.out"
  },
  {
   "label": "E16_visual_L3_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--from-run",
    "20261013_225051_e10_agent_L3_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 1,
   "seconds": 93.6,
   "run_dir": "20261024_042813_e16_visual_L3_xj-gpt-4.1",
   "run_json": false,
   "stats": {
    "calls": 9,
    "usage_records": 9,
    "prompt_tokens": 28437,
    "completion_tokens": 460,
    "cost_usd": 0.2725,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 9,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 9
     }
    }
   },
   "reports": [
    "2026-10-24_e10_shortlist_controls_20261024_024919_e10_agent_L3-H_xj-gpt-5.4.json",
    "2026-10-24_e10_shortlist_controls_20261024_024919_e10_agent_L3-H_xj-gpt-5.4.md",
    "2026-10-24_e10_shortlist_controls_20261024_031349_e10_agent_L5_xj-gpt-5.4.json",
    "2026-10-24_e10_shortlist_controls_20261024_031349_e10_agent_L5_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1_E16_visual_L3_dev.out"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "exp": "E8",
   "argv": [
    "scripts/llm_cf_forced_choice.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--n",
    "100",
    "--withhold-evidence",
    "--mask-creator",
    "--both-orders",
    "--tag",
    "v4"
   ],
   "rc": 1,
   "seconds": 13.6,
   "run_dir": "20261024_042949_e8v2_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator",
   "run_json": false,
   "stats": {
    "calls": 0,
    "usage_records": 0,
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "cost_usd": 0.0,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 0,
     "served_other": 0,
     "served_as": {}
    }
   },
   "reports": [],
   "output": "api_2026-10-24_xj-gpt-4.1_E8v4_noevidence_maskcreator.out"
  }
 ],
 "finished": "2026-10-24T04:29:52+08:00"
}
== api_2026-10-24_xj-gpt-4.1_115805_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-24T11:58:05+08:00",
 "jobs": [
  {
   "label": "E10_agent_L2Ttitle_dev",
   "exp": "E10T",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 123.8,
   "run_dir": "20261024_115806_e10_agent_L2-T_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 32,
    "usage_records": 32,
    "prompt_tokens": 74112,
    "completion_tokens": 1321,
    "cost_usd": 0.7146,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 32,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 32
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L2-T_xj-gpt-4.1.json",
    "2026-10-24_e10_regate_L2-T_xj-gpt-4.1.md",
    "2026-10-24_e10_shortlist_controls_20261024_115806_e10_agent_L2-T_xj-gpt-4.1.json",
    "2026-10-24_e10_shortlist_controls_20261024_115806_e10_agent_L2-T_xj-gpt-4.1.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gpt-4.1.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gpt-4.1.md"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1_E10_agent_L2Ttitle_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_115806_e10_agent_L2-T_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_115806_e10_agent_L2-T_xj-gpt-4.1 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L2Ttitle_test",
   "exp": "E10T",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 375.1,
   "run_dir": "20261024_120013_e10_agent_L2-T_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 91,
    "usage_records": 91,
    "prompt_tokens": 224902,
    "completion_tokens": 7248,
    "cost_usd": 2.2231,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 91,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 91
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L2-T_test_xj-gemini-2.5-flash.json",
    "2026-10-24_e10_regate_L2-T_test_xj-gemini-2.5-flash.md",
    "2026-10-24_e10_regate_L2-T_test_xj-gpt-4.1.json",
    "2026-10-24_e10_regate_L2-T_test_xj-gpt-4.1.md",
    "2026-10-24_e10_regate_L2-T_test_xj-qwen3.5-27b.json",
    "2026-10-24_e10_regate_L2-T_test_xj-qwen3.5-27b.md",
    "2026-10-24_e10_regate_L2-T_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_regate_L2-T_xj-gpt-5.4-mini.md",
    "2026-10-24_e10_regate_L3-H_test_xj-claude-sonnet-4.6.json",
    "2026-10-24_e10_regate_L3-H_test_xj-claude-sonnet-4.6.md",
    "2026-10-24_e10_shortlist_controls_20261024_114720_e10_agent_L2-T_xj-gemini-2.5-flash.json",
    "2026-10-24_e10_shortlist_controls_20261024_114720_e10_agent_L2-T_xj-gemini-2.5-flash.md",
    "2026-10-24_e10_shortlist_controls_20261024_115054_e10_agent_L2-T_xj-qwen3.5-27b.json",
    "2026-10-24_e10_shortlist_controls_20261024_115054_e10_agent_L2-T_xj-qwen3.5-27b.md",
    "2026-10-24_e10_shortlist_controls_20261024_115128_e10_agent_L3-H_xj-claude-sonnet-4.6.json",
    "2026-10-24_e10_shortlist_controls_20261024_115128_e10_agent_L3-H_xj-claude-sonnet-4.6.md",
    "2026-10-24_e10_shortlist_controls_20261024_120013_e10_agent_L2-T_xj-gpt-4.1.json",
    "2026-10-24_e10_shortlist_controls_20261024_120013_e10_agent_L2-T_xj-gpt-4.1.md",
    "2026-10-24_e10_shortlist_controls_20261024_120106_e10_agent_L2-T_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_shortlist_controls_20261024_120106_e10_agent_L2-T_xj-gpt-5.4-mini.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gemini-2.5-flash.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gemini-2.5-flash.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gpt-4.1.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gpt-4.1.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-qwen3.5-27b.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-qwen3.5-27b.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gpt-5.4-mini.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gpt-5.4-mini.md",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-claude-sonnet-4.6.json",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-claude-sonnet-4.6.md",
    "2026-10-24_scale_behavior_L3-H_test.json",
    "2026-10-24_scale_behavior_L3-H_test.md",
    "2026-10-24_scale_behavior_L5_test.json",
    "2026-10-24_scale_behavior_L5_test.md"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1_E10_agent_L2Ttitle_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_120013_e10_agent_L2-T_xj-gpt-4.1 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_120013_e10_agent_L2-T_xj-gpt-4.1 (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-24T12:06:40+08:00"
}
== api_2026-10-24_xj-gpt-4.1_130741_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-24T13:07:41+08:00",
 "jobs": [
  {
   "label": "E10_agent_L2Ttitle_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-4.1_115805_suite.json -> 20261024_115806_e10_agent_L2-T_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L2Ttitle_test",
   "skipped": "done: api_2026-10-24_xj-gpt-4.1_115805_suite.json -> 20261024_120013_e10_agent_L2-T_xj-gpt-4.1"
  }
 ],
 "finished": "2026-10-24T13:07:41+08:00"
}
== api_2026-10-24_xj-gpt-4.1_201315_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-24T20:13:15+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214144_t0_closedbook_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214709_e10_agent_L1_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_215425_e10_agent_L3_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_220353_e10_agent_L3-H_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_221207_e10_agent_L5_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_222258_e10_agent_L1_xj-gpt-4.1"
  }
 ],
 "finished": "2026-10-24T20:13:15+08:00"
}
== api_2026-10-24_xj-gpt-4.1_204901_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-24T20:49:01+08:00",
 "jobs": [
  {
   "label": "E16_visual_L5_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-4.1_040507_suite.json -> 20261024_040531_e16_visual_L5_xj-gpt-4.1"
  },
  {
   "label": "E16_visual_L3_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--from-run",
    "20261013_225051_e10_agent_L3_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 2207.4,
   "run_dir": "20261024_204909_e16_visual_L3_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 511195,
    "completion_tokens": 9261,
    "cost_usd": 4.6617,
    "cache_hits": 9,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-24_attestation_independence.json",
    "2026-10-24_attestation_independence.md",
    "2026-10-24_commons_identity.json",
    "2026-10-24_commons_identity.md",
    "2026-10-24_commons_views.json",
    "2026-10-24_custody_events.json",
    "2026-10-24_custody_events.md",
    "2026-10-24_e10_regate_L3-H2_xj-gemini-3-pro.json",
    "2026-10-24_e10_regate_L3-H2_xj-gemini-3-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_203536_e10_agent_L3-H2_xj-gemini-3-pro.json",
    "2026-10-24_e10_shortlist_controls_20261024_203536_e10_agent_L3-H2_xj-gemini-3-pro.md",
    "2026-10-24_e16_visual_L3_dev_xj-gpt-4.1.json",
    "2026-10-24_e16_visual_L3_dev_xj-gpt-4.1.md",
    "2026-10-24_enrich_records.json",
    "2026-10-24_extra_views.json",
    "2026-10-24_fact_cards.json",
    "2026-10-24_fact_cards.md",
    "2026-10-24_harness_open_L1_xj-claude-opus-4.6.json",
    "2026-10-24_harness_open_L1_xj-claude-opus-4.6.md",
    "2026-10-24_harness_open_L1_xj-gpt-5.4.json",
    "2026-10-24_harness_open_L1_xj-gpt-5.4.md",
    "2026-10-24_llm_reunion_agent_L3-H2_xj-gemini-3-pro.json",
    "2026-10-24_llm_reunion_agent_L3-H2_xj-gemini-3-pro.md",
    "2026-10-24_media_integrity.json",
    "2026-10-24_media_integrity.md",
    "2026-10-24_media_usability.json",
    "2026-10-24_media_usability.md",
    "2026-10-24_membership_evidence.json",
    "2026-10-24_membership_evidence.md",
    "2026-10-24_near_duplicates.json",
    "2026-10-24_near_duplicates.md",
    "2026-10-24_quality_audit.json",
    "2026-10-24_quality_audit.md",
    "2026-10-24_release_validation.json",
    "2026-10-24_release_validation.md",
    "2026-10-24_shortlist_shortcuts.json",
    "2026-10-24_shortlist_shortcuts.md",
    "2026-10-24_temporal_ladder.json",
    "2026-10-24_temporal_ladder.md",
    "2026-10-24_text_screen.json",
    "2026-10-24_text_screen.md",
    "2026-10-24_wikidata_deep.json",
    "2026-10-24_wikidata_deep.md",
    "2026-10-24_wikipedia_dump.json"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1_E16_visual_L3_dev.out"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "exp": "E8",
   "argv": [
    "scripts/llm_cf_forced_choice.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--n",
    "100",
    "--withhold-evidence",
    "--mask-creator",
    "--both-orders",
    "--tag",
    "v4"
   ],
   "rc": 0,
   "seconds": 2964.0,
   "run_dir": "20261024_212551_e8v2_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator",
   "run_json": true,
   "stats": {
    "calls": 600,
    "usage_records": 600,
    "prompt_tokens": 155678,
    "completion_tokens": 27075,
    "cost_usd": 2.3606,
    "cache_hits": 4,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 600,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 600
     }
    }
   },
   "reports": [
    "2026-10-24_cf_forced_choice_analysis_xj-gpt-4.1v4_noevidence_maskcreator.json",
    "2026-10-24_cf_forced_choice_analysis_xj-gpt-4.1v4_noevidence_maskcreator.md",
    "2026-10-24_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator.json",
    "2026-10-24_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator.md",
    "2026-10-24_compare_runs_20261023_030442_vs_20261024_203536.json",
    "2026-10-24_compare_runs_20261023_030442_vs_20261024_203536.md",
    "2026-10-24_compare_runs_20261023_030442_vs_20261024_203536_official_dispersed.json",
    "2026-10-24_compare_runs_20261023_030442_vs_20261024_203536_official_dispersed.md",
    "2026-10-24_compare_runs_20261023_033632_vs_20261024_211338.json",
    "2026-10-24_compare_runs_20261023_033632_vs_20261024_211338.md",
    "2026-10-24_compare_runs_20261023_033632_vs_20261024_211338_official_dispersed.json",
    "2026-10-24_compare_runs_20261023_033632_vs_20261024_211338_official_dispersed.md",
    "2026-10-24_decomposition_dev.json",
    "2026-10-24_decomposition_dev.md",
    "2026-10-24_decomposition_test.json",
    "2026-10-24_decomposition_test.md",
    "2026-10-24_e10_regate_L6_xj-gemini-3-pro.json",
    "2026-10-24_e10_regate_L6_xj-gemini-3-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_211338_e10_agent_L6_xj-gemini-3-pro.json",
    "2026-10-24_e10_shortlist_controls_20261024_211338_e10_agent_L6_xj-gemini-3-pro.md",
    "2026-10-24_literature_enrich.json",
    "2026-10-24_literature_enrich.md",
    "2026-10-24_llm_reunion_agent_L6_xj-gemini-3-pro.json",
    "2026-10-24_llm_reunion_agent_L6_xj-gemini-3-pro.md",
    "2026-10-24_mllm_pair_verify_strata_xj-qwen3.5-397b.json",
    "2026-10-24_mllm_pair_verify_strata_xj-qwen3.5-397b.md",
    "2026-10-24_mllm_pair_verify_xj-qwen3.5-397b.json",
    "2026-10-24_mllm_pair_verify_xj-qwen3.5-397b.md",
    "2026-10-24_truth_strata.json",
    "2026-10-24_truth_strata.md"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1_E8v4_noevidence_maskcreator.out",
   "follow_up": [
    "scripts/llm_cf_forced_choice.py --analyze-run 20261024_212551_e8v2_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-24T22:15:15+08:00"
}
== api_2026-10-24_xj-gpt-4.1_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-24T20:49:01+08:00",
 "jobs": [
  {
   "label": "E16_visual_L5_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-4.1_040507_suite.json -> 20261024_040531_e16_visual_L5_xj-gpt-4.1"
  },
  {
   "label": "E16_visual_L3_dev",
   "exp": "E16",
   "argv": [
    "scripts/e16_visual_reunion.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--from-run",
    "20261013_225051_e10_agent_L3_Qwen_Qwen3-VL-2B-Instruct",
    "--k",
    "8"
   ],
   "rc": 0,
   "seconds": 2207.4,
   "run_dir": "20261024_204909_e16_visual_L3_xj-gpt-4.1",
   "run_json": true,
   "stats": {
    "calls": 160,
    "usage_records": 160,
    "prompt_tokens": 511195,
    "completion_tokens": 9261,
    "cost_usd": 4.6617,
    "cache_hits": 9,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 160,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 160
     }
    }
   },
   "reports": [
    "2026-10-24_attestation_independence.json",
    "2026-10-24_attestation_independence.md",
    "2026-10-24_commons_identity.json",
    "2026-10-24_commons_identity.md",
    "2026-10-24_commons_views.json",
    "2026-10-24_custody_events.json",
    "2026-10-24_custody_events.md",
    "2026-10-24_e10_regate_L3-H2_xj-gemini-3-pro.json",
    "2026-10-24_e10_regate_L3-H2_xj-gemini-3-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_203536_e10_agent_L3-H2_xj-gemini-3-pro.json",
    "2026-10-24_e10_shortlist_controls_20261024_203536_e10_agent_L3-H2_xj-gemini-3-pro.md",
    "2026-10-24_e16_visual_L3_dev_xj-gpt-4.1.json",
    "2026-10-24_e16_visual_L3_dev_xj-gpt-4.1.md",
    "2026-10-24_enrich_records.json",
    "2026-10-24_extra_views.json",
    "2026-10-24_fact_cards.json",
    "2026-10-24_fact_cards.md",
    "2026-10-24_harness_open_L1_xj-claude-opus-4.6.json",
    "2026-10-24_harness_open_L1_xj-claude-opus-4.6.md",
    "2026-10-24_harness_open_L1_xj-gpt-5.4.json",
    "2026-10-24_harness_open_L1_xj-gpt-5.4.md",
    "2026-10-24_llm_reunion_agent_L3-H2_xj-gemini-3-pro.json",
    "2026-10-24_llm_reunion_agent_L3-H2_xj-gemini-3-pro.md",
    "2026-10-24_media_integrity.json",
    "2026-10-24_media_integrity.md",
    "2026-10-24_media_usability.json",
    "2026-10-24_media_usability.md",
    "2026-10-24_membership_evidence.json",
    "2026-10-24_membership_evidence.md",
    "2026-10-24_near_duplicates.json",
    "2026-10-24_near_duplicates.md",
    "2026-10-24_quality_audit.json",
    "2026-10-24_quality_audit.md",
    "2026-10-24_release_validation.json",
    "2026-10-24_release_validation.md",
    "2026-10-24_shortlist_shortcuts.json",
    "2026-10-24_shortlist_shortcuts.md",
    "2026-10-24_temporal_ladder.json",
    "2026-10-24_temporal_ladder.md",
    "2026-10-24_text_screen.json",
    "2026-10-24_text_screen.md",
    "2026-10-24_wikidata_deep.json",
    "2026-10-24_wikidata_deep.md",
    "2026-10-24_wikipedia_dump.json"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1_E16_visual_L3_dev.out"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "exp": "E8",
   "argv": [
    "scripts/llm_cf_forced_choice.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-4.1",
    "--n",
    "100",
    "--withhold-evidence",
    "--mask-creator",
    "--both-orders",
    "--tag",
    "v4"
   ],
   "rc": 0,
   "seconds": 2964.0,
   "run_dir": "20261024_212551_e8v2_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator",
   "run_json": true,
   "stats": {
    "calls": 600,
    "usage_records": 600,
    "prompt_tokens": 155678,
    "completion_tokens": 27075,
    "cost_usd": 2.3606,
    "cache_hits": 4,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-4.1",
     "with_model_returned": 600,
     "served_other": 0,
     "served_as": {
      "gpt-4.1-2025-04-14": 600
     }
    }
   },
   "reports": [
    "2026-10-24_cf_forced_choice_analysis_xj-gpt-4.1v4_noevidence_maskcreator.json",
    "2026-10-24_cf_forced_choice_analysis_xj-gpt-4.1v4_noevidence_maskcreator.md",
    "2026-10-24_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator.json",
    "2026-10-24_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator.md",
    "2026-10-24_compare_runs_20261023_030442_vs_20261024_203536.json",
    "2026-10-24_compare_runs_20261023_030442_vs_20261024_203536.md",
    "2026-10-24_compare_runs_20261023_030442_vs_20261024_203536_official_dispersed.json",
    "2026-10-24_compare_runs_20261023_030442_vs_20261024_203536_official_dispersed.md",
    "2026-10-24_compare_runs_20261023_033632_vs_20261024_211338.json",
    "2026-10-24_compare_runs_20261023_033632_vs_20261024_211338.md",
    "2026-10-24_compare_runs_20261023_033632_vs_20261024_211338_official_dispersed.json",
    "2026-10-24_compare_runs_20261023_033632_vs_20261024_211338_official_dispersed.md",
    "2026-10-24_decomposition_dev.json",
    "2026-10-24_decomposition_dev.md",
    "2026-10-24_decomposition_test.json",
    "2026-10-24_decomposition_test.md",
    "2026-10-24_e10_regate_L6_xj-gemini-3-pro.json",
    "2026-10-24_e10_regate_L6_xj-gemini-3-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_211338_e10_agent_L6_xj-gemini-3-pro.json",
    "2026-10-24_e10_shortlist_controls_20261024_211338_e10_agent_L6_xj-gemini-3-pro.md",
    "2026-10-24_literature_enrich.json",
    "2026-10-24_literature_enrich.md",
    "2026-10-24_llm_reunion_agent_L6_xj-gemini-3-pro.json",
    "2026-10-24_llm_reunion_agent_L6_xj-gemini-3-pro.md",
    "2026-10-24_mllm_pair_verify_strata_xj-qwen3.5-397b.json",
    "2026-10-24_mllm_pair_verify_strata_xj-qwen3.5-397b.md",
    "2026-10-24_mllm_pair_verify_xj-qwen3.5-397b.json",
    "2026-10-24_mllm_pair_verify_xj-qwen3.5-397b.md",
    "2026-10-24_truth_strata.json",
    "2026-10-24_truth_strata.md"
   ],
   "output": "api_2026-10-24_xj-gpt-4.1_E8v4_noevidence_maskcreator.out",
   "follow_up": [
    "scripts/llm_cf_forced_choice.py --analyze-run 20261024_212551_e8v2_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-24T22:15:15+08:00"
}
== api_2026-10-24_xj-gpt-5.4-mini_120105_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-24T12:01:05+08:00",
 "jobs": [
  {
   "label": "E10_agent_L2Ttitle_dev",
   "exp": "E10T",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 283.5,
   "run_dir": "20261024_120106_e10_agent_L2-T_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 32,
    "usage_records": 32,
    "prompt_tokens": 74080,
    "completion_tokens": 24528,
    "cost_usd": 0.7471,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 32,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 32
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L2-T_test_xj-gemini-2.5-flash.json",
    "2026-10-24_e10_regate_L2-T_test_xj-gemini-2.5-flash.md",
    "2026-10-24_e10_regate_L2-T_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_regate_L2-T_xj-gpt-5.4-mini.md",
    "2026-10-24_e10_regate_L3-H_test_xj-claude-sonnet-4.6.json",
    "2026-10-24_e10_regate_L3-H_test_xj-claude-sonnet-4.6.md",
    "2026-10-24_e10_shortlist_controls_20261024_114720_e10_agent_L2-T_xj-gemini-2.5-flash.json",
    "2026-10-24_e10_shortlist_controls_20261024_114720_e10_agent_L2-T_xj-gemini-2.5-flash.md",
    "2026-10-24_e10_shortlist_controls_20261024_115128_e10_agent_L3-H_xj-claude-sonnet-4.6.json",
    "2026-10-24_e10_shortlist_controls_20261024_115128_e10_agent_L3-H_xj-claude-sonnet-4.6.md",
    "2026-10-24_e10_shortlist_controls_20261024_120106_e10_agent_L2-T_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_shortlist_controls_20261024_120106_e10_agent_L2-T_xj-gpt-5.4-mini.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gemini-2.5-flash.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gemini-2.5-flash.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gpt-5.4-mini.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-gpt-5.4-mini.md",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-claude-sonnet-4.6.json",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-claude-sonnet-4.6.md",
    "2026-10-24_scale_behavior_L3-H_test.json",
    "2026-10-24_scale_behavior_L3-H_test.md",
    "2026-10-24_scale_behavior_L5_test.json",
    "2026-10-24_scale_behavior_L5_test.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4-mini_E10_agent_L2Ttitle_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_120106_e10_agent_L2-T_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_120106_e10_agent_L2-T_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L2Ttitle_test",
   "exp": "E10T",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L2-T"
   ],
   "rc": 0,
   "seconds": 736.4,
   "run_dir": "20261024_120553_e10_agent_L2-T_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 91,
    "usage_records": 91,
    "prompt_tokens": 224811,
    "completion_tokens": 50300,
    "cost_usd": 1.7444,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 91,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 91
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L2-T_test_xj-gpt-4.1.json",
    "2026-10-24_e10_regate_L2-T_test_xj-gpt-4.1.md",
    "2026-10-24_e10_regate_L2-T_test_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_regate_L2-T_test_xj-gpt-5.4-mini.md",
    "2026-10-24_e10_regate_L5_test_xj-gemini-3-pro.json",
    "2026-10-24_e10_regate_L5_test_xj-gemini-3-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_115118_e10_agent_L5_xj-gemini-3-pro.json",
    "2026-10-24_e10_shortlist_controls_20261024_115118_e10_agent_L5_xj-gemini-3-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_120013_e10_agent_L2-T_xj-gpt-4.1.json",
    "2026-10-24_e10_shortlist_controls_20261024_120013_e10_agent_L2-T_xj-gpt-4.1.md",
    "2026-10-24_e10_shortlist_controls_20261024_120553_e10_agent_L2-T_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_shortlist_controls_20261024_120553_e10_agent_L2-T_xj-gpt-5.4-mini.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gpt-4.1.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gpt-4.1.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gpt-5.4-mini.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-gpt-5.4-mini.md",
    "2026-10-24_llm_reunion_agent_L5_test_xj-gemini-3-pro.json",
    "2026-10-24_llm_reunion_agent_L5_test_xj-gemini-3-pro.md",
    "2026-10-24_supervised_control_L3-H_test.json",
    "2026-10-24_supervised_control_L3-H_test.md",
    "2026-10-24_supervised_control_L3-H_test_rich_thr.json",
    "2026-10-24_supervised_control_L3-H_test_rich_thr.md",
    "2026-10-24_supervised_control_L3-H_test_thr.json",
    "2026-10-24_supervised_control_L3-H_test_thr.md",
    "2026-10-24_supervised_control_L5_test.json",
    "2026-10-24_supervised_control_L5_test.md",
    "2026-10-24_supervised_control_L5_test_rich_thr.json",
    "2026-10-24_supervised_control_L5_test_rich_thr.md",
    "2026-10-24_supervised_control_L5_test_thr.json",
    "2026-10-24_supervised_control_L5_test_thr.md",
    "2026-10-24_truth_strata.json",
    "2026-10-24_truth_strata.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4-mini_E10_agent_L2Ttitle_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_120553_e10_agent_L2-T_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_120553_e10_agent_L2-T_xj-gpt-5.4-mini (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-24T12:18:25+08:00"
}
== api_2026-10-24_xj-gpt-5.4-mini_130741_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-24T13:07:41+08:00",
 "jobs": [
  {
   "label": "E10_agent_L2Ttitle_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4-mini_120105_suite.json -> 20261024_120106_e10_agent_L2-T_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L2Ttitle_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4-mini_120105_suite.json -> 20261024_120553_e10_agent_L2-T_xj-gpt-5.4-mini"
  }
 ],
 "finished": "2026-10-24T13:07:41+08:00"
}
== api_2026-10-24_xj-gpt-5.4-mini_134727_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-24T13:47:27+08:00",
 "jobs": [
  {
   "label": "E10_agent_L3H_test",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 4190.5,
   "run_dir": "20261024_134728_e10_agent_L3-H_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 531217,
    "completion_tokens": 183011,
    "cost_usd": 5.4789,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 294
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L3-H_test_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_regate_L3-H_test_xj-gpt-5.4-mini.md",
    "2026-10-24_e10_shortlist_controls_20261024_134728_e10_agent_L3-H_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_shortlist_controls_20261024_134728_e10_agent_L3-H_xj-gpt-5.4-mini.md",
    "2026-10-24_ladder_summary.json",
    "2026-10-24_ladder_summary.md",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-gpt-5.4-mini.json",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-gpt-5.4-mini.md",
    "2026-10-24_supervised_control_L5_test.json",
    "2026-10-24_supervised_control_L5_test.md",
    "2026-10-24_truth_strata.json",
    "2026-10-24_truth_strata.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4-mini_E10_agent_L3H_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_134728_e10_agent_L3-H_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_134728_e10_agent_L3-H_xj-gpt-5.4-mini (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4-mini",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 4460.4,
   "run_dir": "20261024_145817_e10_agent_L5_xj-gpt-5.4-mini",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 361748,
    "completion_tokens": 175439,
    "cost_usd": 4.7493,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4-mini",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-mini-2026-03-17": 294
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L3-H_test_xj-gemini-2.5-flash.json",
    "2026-10-24_e10_regate_L3-H_test_xj-gemini-2.5-flash.md",
    "2026-10-24_e10_regate_L5_test_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_regate_L5_test_xj-gpt-5.4-mini.md",
    "2026-10-24_e10_shortlist_controls_20261024_130742_e10_agent_L3-H_xj-gemini-2.5-flash.json",
    "2026-10-24_e10_shortlist_controls_20261024_130742_e10_agent_L3-H_xj-gemini-2.5-flash.md",
    "2026-10-24_e10_shortlist_controls_20261024_145817_e10_agent_L5_xj-gpt-5.4-mini.json",
    "2026-10-24_e10_shortlist_controls_20261024_145817_e10_agent_L5_xj-gpt-5.4-mini.md",
    "2026-10-24_holder_leak_audit.json",
    "2026-10-24_holder_leak_audit.md",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-gemini-2.5-flash.json",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-gemini-2.5-flash.md",
    "2026-10-24_llm_reunion_agent_L5_test_xj-gpt-5.4-mini.json",
    "2026-10-24_llm_reunion_agent_L5_test_xj-gpt-5.4-mini.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4-mini_E10_agent_L5_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_145817_e10_agent_L5_xj-gpt-5.4-mini (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_145817_e10_agent_L5_xj-gpt-5.4-mini (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-24T16:13:22+08:00"
}
== api_2026-10-24_xj-gpt-5.4-mini_194019_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-24T19:40:19+08:00",
 "jobs": [
  {
   "label": "E10_agent_L3H_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4-mini_134727_suite.json -> 20261024_134728_e10_agent_L3-H_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L5_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4-mini_134727_suite.json -> 20261024_145817_e10_agent_L5_xj-gpt-5.4-mini"
  }
 ],
 "finished": "2026-10-24T19:40:19+08:00"
}
== api_2026-10-24_xj-gpt-5.4-mini_201315_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-24T20:13:15+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_205358_t0_closedbook_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini"
  }
 ],
 "finished": "2026-10-24T20:13:15+08:00"
}
== api_2026-10-24_xj-gpt-5.4-mini_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-24T20:13:15+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_205358_t0_closedbook_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini"
  }
 ],
 "finished": "2026-10-24T20:13:15+08:00"
}
== api_2026-10-24_xj-gpt-5.4_024906_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T02:49:06+08:00",
 "jobs": [
  {
   "label": "E10_agent_L3H_test",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H"
   ],
   "rc": 0,
   "seconds": 1390.0,
   "run_dir": "20261024_024919_e10_agent_L3-H_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 531217,
    "completion_tokens": 19244,
    "cost_usd": 5.1443,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 203,
      "gpt-5.4": 91
     }
    }
   },
   "reports": [
    "2026-10-24_cf_forced_choice_analysis_xj-claude-sonnet-4.6v4_noevidence_maskcreator.json",
    "2026-10-24_cf_forced_choice_analysis_xj-claude-sonnet-4.6v4_noevidence_maskcreator.md",
    "2026-10-24_cf_forced_choice_analysis_xj-gemini-2.5-flashv4.json",
    "2026-10-24_cf_forced_choice_analysis_xj-gemini-2.5-flashv4.md",
    "2026-10-24_cf_forced_choice_xj-claude-sonnet-4.6v4_noevidence_maskcreator.json",
    "2026-10-24_cf_forced_choice_xj-claude-sonnet-4.6v4_noevidence_maskcreator.md",
    "2026-10-24_cf_forced_choice_xj-gemini-2.5-flashv4.json",
    "2026-10-24_cf_forced_choice_xj-gemini-2.5-flashv4.md",
    "2026-10-24_e10_regate_L2-T_xj-claude-sonnet-4.6.json",
    "2026-10-24_e10_regate_L2-T_xj-claude-sonnet-4.6.md",
    "2026-10-24_e10_regate_L3-H_test_xj-gemini-3-pro.json",
    "2026-10-24_e10_regate_L3-H_test_xj-gemini-3-pro.md",
    "2026-10-24_e10_regate_L3-H_test_xj-gpt-5.4.json",
    "2026-10-24_e10_regate_L3-H_test_xj-gpt-5.4.md",
    "2026-10-24_e10_regate_L5_xj-gemini-2.5-flash-thinking.json",
    "2026-10-24_e10_regate_L5_xj-gemini-2.5-flash-thinking.md",
    "2026-10-24_e10_shortlist_controls_20261024_005009_e10_agent_L3-H_xj-gemini-3-pro.json",
    "2026-10-24_e10_shortlist_controls_20261024_005009_e10_agent_L3-H_xj-gemini-3-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_021631_e10_agent_L5_xj-gemini-2.5-flash-thinking.json",
    "2026-10-24_e10_shortlist_controls_20261024_021631_e10_agent_L5_xj-gemini-2.5-flash-thinking.md",
    "2026-10-24_e10_shortlist_controls_20261024_024919_e10_agent_L3-H_xj-gpt-5.4.json",
    "2026-10-24_e10_shortlist_controls_20261024_024919_e10_agent_L3-H_xj-gpt-5.4.md",
    "2026-10-24_e10_shortlist_controls_20261024_030705_e10_agent_L2-T_xj-claude-sonnet-4.6.json",
    "2026-10-24_e10_shortlist_controls_20261024_030705_e10_agent_L2-T_xj-claude-sonnet-4.6.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-claude-sonnet-4.6.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-claude-sonnet-4.6.md",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-gemini-3-pro.json",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-gemini-3-pro.md",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-gpt-5.4.json",
    "2026-10-24_llm_reunion_agent_L3-H_test_xj-gpt-5.4.md",
    "2026-10-24_llm_reunion_agent_L5_xj-gemini-2.5-flash-thinking.json",
    "2026-10-24_llm_reunion_agent_L5_xj-gemini-2.5-flash-thinking.md",
    "2026-10-24_mllm_pair_verify_strata_xj-qwen3.5-122b.json",
    "2026-10-24_mllm_pair_verify_strata_xj-qwen3.5-122b.md",
    "2026-10-24_mllm_pair_verify_xj-qwen3.5-122b.json",
    "2026-10-24_mllm_pair_verify_xj-qwen3.5-122b.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4_E10_agent_L3H_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_024919_e10_agent_L3-H_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_024919_e10_agent_L3-H_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L5_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5"
   ],
   "rc": 0,
   "seconds": 1341.4,
   "run_dir": "20261024_031349_e10_agent_L5_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 294,
    "usage_records": 294,
    "prompt_tokens": 361748,
    "completion_tokens": 18290,
    "cost_usd": 3.7505,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 294,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 210,
      "gpt-5.4": 84
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L2-T_test_xj-claude-sonnet-4.6.json",
    "2026-10-24_e10_regate_L2-T_test_xj-claude-sonnet-4.6.md",
    "2026-10-24_e10_regate_L3-H_test_mimo-v2.6-pro.json",
    "2026-10-24_e10_regate_L3-H_test_mimo-v2.6-pro.md",
    "2026-10-24_e10_regate_L5_test_xj-gpt-5.4.json",
    "2026-10-24_e10_regate_L5_test_xj-gpt-5.4.md",
    "2026-10-24_e10_shortlist_controls_20261024_025311_e10_agent_L3-H_mimo-v2.6-pro.json",
    "2026-10-24_e10_shortlist_controls_20261024_025311_e10_agent_L3-H_mimo-v2.6-pro.md",
    "2026-10-24_e10_shortlist_controls_20261024_031335_e10_agent_L2-T_xj-claude-sonnet-4.6.json",
    "2026-10-24_e10_shortlist_controls_20261024_031335_e10_agent_L2-T_xj-claude-sonnet-4.6.md",
    "2026-10-24_e10_shortlist_controls_20261024_031349_e10_agent_L5_xj-gpt-5.4.json",
    "2026-10-24_e10_shortlist_controls_20261024_031349_e10_agent_L5_xj-gpt-5.4.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-claude-sonnet-4.6.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-claude-sonnet-4.6.md",
    "2026-10-24_llm_reunion_agent_L3-H_test_mimo-v2.6-pro.json",
    "2026-10-24_llm_reunion_agent_L3-H_test_mimo-v2.6-pro.md",
    "2026-10-24_llm_reunion_agent_L5_test_xj-gpt-5.4.json",
    "2026-10-24_llm_reunion_agent_L5_test_xj-gpt-5.4.md",
    "2026-10-24_t5_llm_profile_L1_xj-gemini-2.5-flash.json",
    "2026-10-24_t5_llm_profile_L1_xj-gemini-2.5-flash.md",
    "2026-10-24_t5_profile_replay_L1_xj-gemini-2.5-flash.json",
    "2026-10-24_t5_profile_replay_L1_xj-gemini-2.5-flash.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4_E10_agent_L5_test.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_031349_e10_agent_L5_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_031349_e10_agent_L5_xj-gpt-5.4 (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-24T03:37:20+08:00"
}
== api_2026-10-24_xj-gpt-5.4_115122_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T11:51:22+08:00",
 "jobs": [
  {
   "label": "E10_agent_L3H_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_024906_suite.json -> 20261024_024919_e10_agent_L3-H_xj-gpt-5.4"
  },
  {
   "label": "E10_agent_L5_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_024906_suite.json -> 20261024_031349_e10_agent_L5_xj-gpt-5.4"
  }
 ],
 "finished": "2026-10-24T11:51:22+08:00"
}
== api_2026-10-24_xj-gpt-5.4_130736_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T13:07:36+08:00",
 "jobs": [
  {
   "label": "E10_agent_L3H_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_024906_suite.json -> 20261024_024919_e10_agent_L3-H_xj-gpt-5.4"
  },
  {
   "label": "E10_agent_L5_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_024906_suite.json -> 20261024_031349_e10_agent_L5_xj-gpt-5.4"
  }
 ],
 "finished": "2026-10-24T13:07:36+08:00"
}
== api_2026-10-24_xj-gpt-5.4_164053_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T16:40:53+08:00",
 "jobs": [
  {
   "label": "E10_agent_L5P_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5",
    "--dims-permute",
    "20261024"
   ],
   "rc": 0,
   "seconds": 378.8,
   "run_dir": "20261024_164053_e10_agent_L5-P_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 97528,
    "completion_tokens": 5215,
    "cost_usd": 1.0186,
    "cache_hits": 2,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 73,
      "gpt-5.4": 7
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L3-H_test_xj-qwen3.5-397b.json",
    "2026-10-24_e10_regate_L3-H_test_xj-qwen3.5-397b.md",
    "2026-10-24_e10_regate_L5-P_xj-gpt-5.4.json",
    "2026-10-24_e10_regate_L5-P_xj-gpt-5.4.md",
    "2026-10-24_e10_shortlist_controls_20261024_161323_e10_agent_L3-H_xj-qwen3.5-397b.json",
    "2026-10-24_e10_shortlist_controls_20261024_161323_e10_agent_L3-H_xj-qwen3.5-397b.md",
    "2026-10-24_e10_shortlist_controls_20261024_164053_e10_agent_L5-P_xj-gpt-5.4.json",
    "2026-10-24_e10_shortlist_controls_20261024_164053_e10_agent_L5-P_xj-gpt-5.4.md",
    "2026-10-24_llm_reunion_agent_L5-P_xj-gpt-5.4.json",
    "2026-10-24_llm_reunion_agent_L5-P_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4_E10_agent_L5P_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_164053_e10_agent_L5-P_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_164053_e10_agent_L5-P_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L3H2_dev",
   "exp": "E10H",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L3-H",
    "--holder-scrub",
    "v2"
   ],
   "rc": 0,
   "seconds": 334.2,
   "run_dir": "20261024_164732_e10_agent_L3-H2_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 136370,
    "completion_tokens": 5474,
    "cost_usd": 1.2707,
    "cache_hits": 8,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 77,
      "gpt-5.4": 3
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L3-H2_xj-gpt-5.4.json",
    "2026-10-24_e10_regate_L3-H2_xj-gpt-5.4.md",
    "2026-10-24_e10_shortlist_controls_20261024_164732_e10_agent_L3-H2_xj-gpt-5.4.json",
    "2026-10-24_e10_shortlist_controls_20261024_164732_e10_agent_L3-H2_xj-gpt-5.4.md",
    "2026-10-24_llm_reunion_agent_L3-H2_xj-gpt-5.4.json",
    "2026-10-24_llm_reunion_agent_L3-H2_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4_E10_agent_L3H2_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_164732_e10_agent_L3-H2_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_164732_e10_agent_L3-H2_xj-gpt-5.4 (rc=0)"
   ]
  },
  {
   "label": "E10_agent_L6_dev",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "dev",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5",
    "--withhold-title"
   ],
   "rc": 0,
   "seconds": 1606.4,
   "run_dir": "20261024_165325_e10_agent_L6_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 80,
    "usage_records": 80,
    "prompt_tokens": 85089,
    "completion_tokens": 4421,
    "cost_usd": 0.8929,
    "cache_hits": 0,
    "api_errors": 0,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 80,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 80
     }
    }
   },
   "reports": [
    "2026-10-24_e10_regate_L6_xj-gpt-5.4.json",
    "2026-10-24_e10_regate_L6_xj-gpt-5.4.md",
    "2026-10-24_e10_shortlist_controls_20261024_165325_e10_agent_L6_xj-gpt-5.4.json",
    "2026-10-24_e10_shortlist_controls_20261024_165325_e10_agent_L6_xj-gpt-5.4.md",
    "2026-10-24_llm_reunion_agent_L6_xj-gpt-5.4.json",
    "2026-10-24_llm_reunion_agent_L6_xj-gpt-5.4.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4_E10_agent_L6_dev.out",
   "follow_up": [
    "scripts/e10_regate.py --run 20261024_165325_e10_agent_L6_xj-gpt-5.4 (rc=0)",
    "scripts/e10_shortlist_controls.py --run 20261024_165325_e10_agent_L6_xj-gpt-5.4 (rc=0)"
   ]
  }
 ],
 "finished": "2026-10-24T17:20:25+08:00"
}
== api_2026-10-24_xj-gpt-5.4_194009_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T19:40:09+08:00",
 "jobs": [
  {
   "label": "E10_agent_L5P_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_164053_suite.json -> 20261024_164053_e10_agent_L5-P_xj-gpt-5.4"
  },
  {
   "label": "E10_agent_L3H2_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_164053_suite.json -> 20261024_164732_e10_agent_L3-H2_xj-gpt-5.4"
  },
  {
   "label": "E10_agent_L6_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_164053_suite.json -> 20261024_165325_e10_agent_L6_xj-gpt-5.4"
  }
 ],
 "finished": "2026-10-24T19:40:09+08:00"
}
== api_2026-10-24_xj-gpt-5.4_194014_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T19:40:14+08:00",
 "jobs": [
  {
   "label": "E10_agent_L3H_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_024906_suite.json -> 20261024_024919_e10_agent_L3-H_xj-gpt-5.4"
  },
  {
   "label": "E10_agent_L5_test",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_024906_suite.json -> 20261024_031349_e10_agent_L5_xj-gpt-5.4"
  }
 ],
 "finished": "2026-10-24T19:40:14+08:00"
}
== api_2026-10-24_xj-gpt-5.4_203935_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T20:39:35+08:00",
 "jobs": [
  {
   "label": "E17_open_L1_dev20",
   "exp": "E17",
   "argv": [
    "scripts/deep_research_harness.py",
    "--policy",
    "llm",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--level",
    "L1",
    "--split",
    "dev",
    "--limit",
    "20",
    "--stride",
    "4",
    "--max-steps",
    "14",
    "--max-tokens",
    "220",
    "--pool",
    "open"
   ],
   "rc": 0,
   "seconds": 1063.5,
   "run_dir": "20261024_203938_harness_open_L1_xj-gpt-5.4",
   "run_json": true,
   "stats": {
    "calls": 20,
    "usage_records": 211,
    "prompt_tokens": 500102,
    "completion_tokens": 9239,
    "cost_usd": 4.4005,
    "cache_hits": 9,
    "api_errors": 2,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 209,
     "served_other": 0,
     "served_as": {
      "gpt-5.4-2026-03-05": 209
     }
    }
   },
   "reports": [
    "2026-10-24_commons_views.json",
    "2026-10-24_custody_events.json",
    "2026-10-24_custody_events.md",
    "2026-10-24_e10_regate_L2-T_test_xj-qwen3.5-122b.json",
    "2026-10-24_e10_regate_L2-T_test_xj-qwen3.5-122b.md",
    "2026-10-24_e10_regate_L2-T_xj-qwen3.5-122b.json",
    "2026-10-24_e10_regate_L2-T_xj-qwen3.5-122b.md",
    "2026-10-24_e10_shortlist_controls_20261024_203533_e10_agent_L2-T_xj-qwen3.5-122b.json",
    "2026-10-24_e10_shortlist_controls_20261024_203533_e10_agent_L2-T_xj-qwen3.5-122b.md",
    "2026-10-24_e10_shortlist_controls_20261024_204417_e10_agent_L2-T_xj-qwen3.5-122b.json",
    "2026-10-24_e10_shortlist_controls_20261024_204417_e10_agent_L2-T_xj-qwen3.5-122b.md",
    "2026-10-24_enrich_records.json",
    "2026-10-24_extra_views.json",
    "2026-10-24_harness_L1_xj-claude-sonnet-4.6.json",
    "2026-10-24_harness_L1_xj-claude-sonnet-4.6.md",
    "2026-10-24_harness_open_L1_xj-gpt-5.4.json",
    "2026-10-24_harness_open_L1_xj-gpt-5.4.md",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-qwen3.5-122b.json",
    "2026-10-24_llm_reunion_agent_L2-T_test_xj-qwen3.5-122b.md",
    "2026-10-24_llm_reunion_agent_L2-T_xj-qwen3.5-122b.json",
    "2026-10-24_llm_reunion_agent_L2-T_xj-qwen3.5-122b.md",
    "2026-10-24_media_integrity.json",
    "2026-10-24_media_integrity.md",
    "2026-10-24_oa_fulltext.json",
    "2026-10-24_wikidata_deep.json",
    "2026-10-24_wikidata_deep.md",
    "2026-10-24_wikipedia_dump.json"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4_E17_open_L1_dev20.out"
  }
 ],
 "finished": "2026-10-24T20:57:18+08:00"
}
== api_2026-10-24_xj-gpt-5.4_215306_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T21:53:06+08:00",
 "jobs": [
  {
   "label": "E10_agent_L5P_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_164053_suite.json -> 20261024_164053_e10_agent_L5-P_xj-gpt-5.4"
  },
  {
   "label": "E10_agent_L3H2_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_164053_suite.json -> 20261024_164732_e10_agent_L3-H2_xj-gpt-5.4"
  },
  {
   "label": "E10_agent_L6_dev",
   "skipped": "done: api_2026-10-24_xj-gpt-5.4_164053_suite.json -> 20261024_165325_e10_agent_L6_xj-gpt-5.4"
  }
 ],
 "finished": "2026-10-24T21:53:07+08:00"
}
== api_2026-10-24_xj-gpt-5.4_234810_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T23:48:10+08:00",
 "jobs": [
  {
   "label": "E10_agent_L5P_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5",
    "--dims-permute",
    "20261024"
   ],
   "rc": 1,
   "seconds": 504.9,
   "run_dir": "20261024_234820_e10_agent_L5-P_xj-gpt-5.4",
   "run_json": false,
   "stats": {
    "calls": 4,
    "usage_records": 4,
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "cost_usd": 0.0,
    "cache_hits": 0,
    "api_errors": 4,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 0,
     "served_other": 0,
     "served_as": {}
    }
   },
   "reports": [
    "2026-10-24_token_efficiency_test.json",
    "2026-10-24_token_efficiency_test.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4_E10_agent_L5P_test.out"
  }
 ],
 "finished": "2026-10-24T23:56:35+08:00"
}
== api_2026-10-24_xj-gpt-5.4_suite.json
{
 "alias": "xj-gpt-5.4",
 "provider_model": "gpt-5.4",
 "family": "OpenAI GPT-5.4 via xiaojingai relay (OpenAI flagship of the same generation as xj-gpt-5.4-mini; s42 10-22: probed, served gpt-5.4, 4 output tokens, no hidden-reasoning tax on a short call). Price estimated. fixed_temperature because the gpt-5 family rejects temperature.",
 "smoke": false,
 "started": "2026-10-24T23:48:10+08:00",
 "jobs": [
  {
   "label": "E10_agent_L5P_test",
   "exp": "E10",
   "argv": [
    "scripts/llm_reunion_agent.py",
    "--backend",
    "api",
    "--model",
    "xj-gpt-5.4",
    "--split",
    "test",
    "--limit",
    "0",
    "--k",
    "30",
    "--level",
    "L5",
    "--dims-permute",
    "20261024"
   ],
   "rc": 1,
   "seconds": 504.9,
   "run_dir": "20261024_234820_e10_agent_L5-P_xj-gpt-5.4",
   "run_json": false,
   "stats": {
    "calls": 4,
    "usage_records": 4,
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "cost_usd": 0.0,
    "cache_hits": 0,
    "api_errors": 4,
    "served_model_audit": {
     "requested": "gpt-5.4",
     "with_model_returned": 0,
     "served_other": 0,
     "served_as": {}
    }
   },
   "reports": [
    "2026-10-24_token_efficiency_test.json",
    "2026-10-24_token_efficiency_test.md"
   ],
   "output": "api_2026-10-24_xj-gpt-5.4_E10_agent_L5P_test.out"
  }
 ],
 "finished": "2026-10-24T23:56:35+08:00"
}
== api_2026-10-25_xj-gpt-4.1-mini_002023_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-25T00:20:23+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_110754_t0_closedbook_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_111332_e10_agent_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112119_e10_agent_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_112731_e10_agent_L3-H_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_113410_e10_agent_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_110754_suite.json -> 20261022_114037_e10_agent_L1_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-25T00:20:24+08:00"
}
== api_2026-10-25_xj-gpt-4.1-mini_002039_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-25T00:20:39+08:00",
 "jobs": [
  {
   "label": "E10_agent_L1_dev_v1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1"
  },
  {
   "label": "E10_agent_L1_dev_v2",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2"
  },
  {
   "label": "E10_agent_L1_dev_rep1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1"
  },
  {
   "label": "E16_visual_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_225050_e16_visual_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_230933_e16_visual_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_232828_e16_visual_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator"
  },
  {
   "label": "E15_harness_L1_dev40",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_002216_harness_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E7_pair_verify_balanced",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_003611_c4_pair_verify_xj-gpt-4.1-mini"
  },
  {
   "label": "E10e_pointwise_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10c_visual_score",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_032614_e10c_visual_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E15_harness_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034446_harness_L2T_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_L1_both_orders",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4"
  },
  {
   "label": "E9_T5_profile_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042523_t1_rerank_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L5",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042821_t1_rerank_L5_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-25T00:20:40+08:00"
}
== api_2026-10-25_xj-gpt-4.1-mini_suite.json
{
 "alias": "xj-gpt-4.1-mini",
 "provider_model": "gpt-4.1-mini",
 "family": "OpenAI GPT-4.1 mini via xiaojingai relay (OpenAI family, small; preflight 10-22: logprobs passed through -> first-token P(yes), same definition as the local runs)",
 "smoke": false,
 "started": "2026-10-25T00:20:39+08:00",
 "jobs": [
  {
   "label": "E10_agent_L1_dev_v1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_223403_e10_agent_L1_xj-gpt-4.1-mini_v1"
  },
  {
   "label": "E10_agent_L1_dev_v2",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224025_e10_agent_L1_xj-gpt-4.1-mini_v2"
  },
  {
   "label": "E10_agent_L1_dev_rep1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_224522_e10_agent_L1_xj-gpt-4.1-mini_rep1"
  },
  {
   "label": "E16_visual_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_225050_e16_visual_L5_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_230933_e16_visual_L3_xj-gpt-4.1-mini"
  },
  {
   "label": "E16_visual_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_232828_e16_visual_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_noevidence_maskcreator",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261022_234756_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4_noevidence_maskcreator"
  },
  {
   "label": "E15_harness_L1_dev40",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_002216_harness_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E7_pair_verify_balanced",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_003611_c4_pair_verify_xj-gpt-4.1-mini"
  },
  {
   "label": "E10e_pointwise_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E10c_visual_score",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_032614_e10c_visual_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034308_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E10_agent_L2T_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034328_e10_agent_L2-T_xj-gpt-4.1-mini"
  },
  {
   "label": "E15_harness_L2T_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034446_harness_L2T_xj-gpt-4.1-mini"
  },
  {
   "label": "E8v4_L1_both_orders",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_034653_e8v2_cf_forced_choice_xj-gpt-4.1-miniv4"
  },
  {
   "label": "E9_T5_profile_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_041758_e9_t5_profile_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L1",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042523_t1_rerank_L1_xj-gpt-4.1-mini"
  },
  {
   "label": "E6_rerank_L5",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1-mini_223401_suite.json -> 20261023_042821_t1_rerank_L5_xj-gpt-4.1-mini"
  }
 ],
 "finished": "2026-10-25T00:20:40+08:00"
}
== api_2026-10-25_xj-gpt-4.1_002034_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-25T00:20:34+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214144_t0_closedbook_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214709_e10_agent_L1_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_215425_e10_agent_L3_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_220353_e10_agent_L3-H_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_221207_e10_agent_L5_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_222258_e10_agent_L1_xj-gpt-4.1"
  }
 ],
 "finished": "2026-10-25T00:20:34+08:00"
}
== api_2026-10-25_xj-gpt-4.1_suite.json
{
 "alias": "xj-gpt-4.1",
 "provider_model": "gpt-4.1",
 "family": "OpenAI GPT-4.1 via xiaojingai relay (OpenAI family, large; relay rate 9 / 36: decisive jobs only)",
 "smoke": false,
 "started": "2026-10-25T00:20:34+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214144_t0_closedbook_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_214709_e10_agent_L1_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_215425_e10_agent_L3_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_220353_e10_agent_L3-H_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_221207_e10_agent_L5_xj-gpt-4.1"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-4.1_214144_suite.json -> 20261022_222258_e10_agent_L1_xj-gpt-4.1"
  }
 ],
 "finished": "2026-10-25T00:20:34+08:00"
}
== api_2026-10-25_xj-gpt-5.4-mini_002034_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-25T00:20:34+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_205358_t0_closedbook_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini"
  }
 ],
 "finished": "2026-10-25T00:20:34+08:00"
}
== api_2026-10-25_xj-gpt-5.4-mini_suite.json
{
 "alias": "xj-gpt-5.4-mini",
 "provider_model": "gpt-5.4-mini",
 "family": "OpenAI GPT-5.4 mini via xiaojingai relay (reasoning model: no temperature, hidden reasoning tokens, reasoning_effort low; thinking-class column)",
 "smoke": false,
 "started": "2026-10-25T00:20:34+08:00",
 "jobs": [
  {
   "label": "E5_closedbook",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_205358_t0_closedbook_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_210157_e10_agent_L1_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_211105_e10_agent_L3_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L3H_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212019_e10_agent_L3-H_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L5_dev",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_212916_e10_agent_L5_xj-gpt-5.4-mini"
  },
  {
   "label": "E10_agent_L1_test",
   "skipped": "done: api_2026-10-22_xj-gpt-5.4-mini_205358_suite.json -> 20261022_214027_e10_agent_L1_xj-gpt-5.4-mini"
  }
 ],
 "finished": "2026-10-25T00:20:34+08:00"
}
== api_campaign_pt.state.json
{
 "plan": "configs\\campaign_s45_l5perm_test.json",
 "attempt": 2,
 "started": "2026-10-25 00:20:28",
 "complete": false,
 "halted": null,
 "rc": {}
}
```
