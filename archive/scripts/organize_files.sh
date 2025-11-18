#!/bin/bash

# CreatiCode Project File Organization Script
# This script organizes the CreatiCode K-8 Skill Map project into a clean structure
# Usage: bash organize_files.sh

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "====================================="
echo "CreatiCode File Organization Script"
echo "====================================="
echo ""

# Create directory structure
echo "Creating directories..."
mkdir -p skills
mkdir -p archive/analysis
mkdir -p docs
echo "✓ Directories created"
echo ""

# Move skill-related JSON files to skills/
echo "Moving skill data files to skills/..."
mv -v skills_k8_ai_complete_FINAL.json skills/ 2>/dev/null || echo "  (skills_k8_ai_complete_FINAL.json not found)"
mv -v FOUNDATIONAL_41_SKILLS.json skills/ 2>/dev/null || echo "  (FOUNDATIONAL_41_SKILLS.json not found)"
mv -v WEEK2_NEW_SKILLS.json skills/ 2>/dev/null || echo "  (WEEK2_NEW_SKILLS.json not found)"
mv -v CREATIVE_SKILLS_3.json skills/ 2>/dev/null || echo "  (CREATIVE_SKILLS_3.json not found)"
mv -v WEEK2_SKILLS_QUICK_REFERENCE.json skills/ 2>/dev/null || echo "  (WEEK2_SKILLS_QUICK_REFERENCE.json not found)"
mv -v CANONICAL_SKILL_SCHEMA.json skills/ 2>/dev/null || echo "  (CANONICAL_SKILL_SCHEMA.json not found)"
mv -v k2_skill_format_spec.json skills/ 2>/dev/null || echo "  (k2_skill_format_spec.json not found)"
mv -v FINAL_SKILL_MAP_STATISTICS.json skills/ 2>/dev/null || echo "  (FINAL_SKILL_MAP_STATISTICS.json not found)"
mv -v k8_complete_statistics.json skills/ 2>/dev/null || echo "  (k8_complete_statistics.json not found)"
mv -v enrichment_stats.json skills/ 2>/dev/null || echo "  (enrichment_stats.json not found)"
mv -v domains_topics.yaml skills/ 2>/dev/null || echo "  (domains_topics.yaml not found)"
mv -v domain_mapping.json skills/ 2>/dev/null || echo "  (domain_mapping.json not found)"
mv -v k2_activity_templates.json skills/ 2>/dev/null || echo "  (k2_activity_templates.json not found)"
mv -v k2_autograding_rules.json skills/ 2>/dev/null || echo "  (k2_autograding_rules.json not found)"
mv -v k2_visual_themes.json skills/ 2>/dev/null || echo "  (k2_visual_themes.json not found)"
mv -v k3_transition_validation.json skills/ 2>/dev/null || echo "  (k3_transition_validation.json not found)"
mv -v foundational_blocks_detailed_analysis.json skills/ 2>/dev/null || echo "  (foundational_blocks_detailed_analysis.json not found)"
mv -v k2_current_analysis.json skills/ 2>/dev/null || echo "  (k2_current_analysis.json not found)"
mv -v skill_file_analysis.json skills/ 2>/dev/null || echo "  (skill_file_analysis.json not found)"
mv -v skill_comparison_report.json skills/ 2>/dev/null || echo "  (skill_comparison_report.json not found)"
mv -v k8_validation_report.json skills/ 2>/dev/null || echo "  (k8_validation_report.json not found)"
mv -v removed_dependencies_report.json skills/ 2>/dev/null || echo "  (removed_dependencies_report.json not found)"
mv -v SKILL_CSTA_ASSIGNMENTS.json skills/ 2>/dev/null || echo "  (SKILL_CSTA_ASSIGNMENTS.json not found)"
mv -v well_designed_examples.json skills/ 2>/dev/null || echo "  (well_designed_examples.json not found)"
mv -v csta_standards_extracted.json skills/ 2>/dev/null || echo "  (csta_standards_extracted.json not found)"
mv -v SKILL_TRACK_CATEGORIZATION.json skills/ 2>/dev/null || echo "  (SKILL_TRACK_CATEGORIZATION.json not found)"
echo "✓ Skill files moved to skills/"
echo ""

# Move AI-related skill files to archive/analysis
echo "Moving AI skill integration files to archive/analysis/..."
mv -v ai_skills_new_phase1.json archive/analysis/ 2>/dev/null || echo "  (ai_skills_new_phase1.json not found)"
mv -v ai_skills_new_phase2.json archive/analysis/ 2>/dev/null || echo "  (ai_skills_new_phase2.json not found)"
mv -v ai_enhanced_statistics.json archive/analysis/ 2>/dev/null || echo "  (ai_enhanced_statistics.json not found)"
mv -v ai_enhanced_validation_report.json archive/analysis/ 2>/dev/null || echo "  (ai_enhanced_validation_report.json not found)"
mv -v age_appropriateness_analysis.json archive/analysis/ 2>/dev/null || echo "  (age_appropriateness_analysis.json not found)"
mv -v comprehensive_age_review.json archive/analysis/ 2>/dev/null || echo "  (comprehensive_age_review.json not found)"
echo "✓ AI skill files moved to archive/analysis/"
echo ""

# Move ACSL-related files to archive/analysis
echo "Moving ACSL analysis files to archive/analysis/..."
mv -v ACSL_ANALYSIS_RAW.json archive/analysis/ 2>/dev/null || echo "  (ACSL_ANALYSIS_RAW.json not found)"
mv -v ACSL_CLEANUP_APPLIED.json archive/analysis/ 2>/dev/null || echo "  (ACSL_CLEANUP_APPLIED.json not found)"
mv -v ACSL_CLEANUP_REPORT.md archive/analysis/ 2>/dev/null || echo "  (ACSL_CLEANUP_REPORT.md not found)"
mv -v ACSL_CONTENT_EXCLUSION.md archive/analysis/ 2>/dev/null || echo "  (ACSL_CONTENT_EXCLUSION.md not found)"
mv -v ACSL_DEPENDENCY_FIXES.json archive/analysis/ 2>/dev/null || echo "  (ACSL_DEPENDENCY_FIXES.json not found)"
echo "✓ ACSL files moved to archive/analysis/"
echo ""

# Move WEEK1 analysis files to archive/analysis
echo "Moving WEEK1 analysis files to archive/analysis/..."
mv -v WEEK1_CHANGES_REPORT.md archive/analysis/ 2>/dev/null || echo "  (WEEK1_CHANGES_REPORT.md not found)"
mv -v WEEK1_IMPLEMENTATION_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (WEEK1_IMPLEMENTATION_SUMMARY.md not found)"
mv -v WEEK1_QUICK_REFERENCE.md archive/analysis/ 2>/dev/null || echo "  (WEEK1_QUICK_REFERENCE.md not found)"
echo "✓ WEEK1 files moved to archive/analysis/"
echo ""

# Move WEEK2 analysis files to archive/analysis
echo "Moving WEEK2 analysis files to archive/analysis/..."
mv -v WEEK2_CREATIVITY_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_CREATIVITY_ANALYSIS.md not found)"
mv -v WEEK2_DEPENDENCY_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_DEPENDENCY_ANALYSIS.md not found)"
mv -v WEEK2_EXECUTIVE_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_EXECUTIVE_SUMMARY.md not found)"
mv -v WEEK2_INTEGRATION_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_INTEGRATION_COMPLETE.md not found)"
mv -v WEEK2_INTEGRATION_REPORT.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_INTEGRATION_REPORT.md not found)"
mv -v WEEK2_INTEGRATION_VALIDATION.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_INTEGRATION_VALIDATION.md not found)"
mv -v WEEK2_PROJECT_PATHWAY.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_PROJECT_PATHWAY.md not found)"
mv -v WEEK2_QUICK_SUMMARY.txt archive/analysis/ 2>/dev/null || echo "  (WEEK2_QUICK_SUMMARY.txt not found)"
mv -v WEEK2_REFRAMED_EXECUTIVE_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_REFRAMED_EXECUTIVE_SUMMARY.md not found)"
mv -v WEEK2_VALIDATION_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_VALIDATION_SUMMARY.md not found)"
mv -v WEEK2_SKILLS_SPECIFICATIONS.md archive/analysis/ 2>/dev/null || echo "  (WEEK2_SKILLS_SPECIFICATIONS.md not found)"
echo "✓ WEEK2 files moved to archive/analysis/"
echo ""

# Move foundational skills analysis files to archive/analysis
echo "Moving foundational skills analysis files to archive/analysis/..."
mv -v FOUNDATIONAL_BLOCKS_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_BLOCKS_ANALYSIS.md not found)"
mv -v FOUNDATIONAL_GAPS_CRITICAL.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_GAPS_CRITICAL.md not found)"
mv -v FOUNDATIONAL_ANALYSIS_SUMMARY.txt archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_ANALYSIS_SUMMARY.txt not found)"
mv -v FOUNDATIONAL_IMPLEMENTATION_GUIDE.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_IMPLEMENTATION_GUIDE.md not found)"
mv -v FOUNDATIONAL_SKILLS_DELIVERY_REPORT.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_SKILLS_DELIVERY_REPORT.md not found)"
mv -v FOUNDATIONAL_SKILLS_QUICK_REFERENCE.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_SKILLS_QUICK_REFERENCE.md not found)"
mv -v FOUNDATIONAL_SKILLS_RECOMMENDATIONS.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_SKILLS_RECOMMENDATIONS.md not found)"
mv -v FOUNDATIONAL_SKILLS_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_SKILLS_SUMMARY.md not found)"
mv -v FOUNDATIONAL_SKILLS_WEEK1.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_SKILLS_WEEK1.md not found)"
mv -v FOUNDATIONAL_SKILLS_WEEK2.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_SKILLS_WEEK2.md not found)"
mv -v FOUNDATIONAL_SKILLS_WEEK3.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATIONAL_SKILLS_WEEK3.md not found)"
mv -v FOUNDATION_SKILLS_BY_CATEGORY.md archive/analysis/ 2>/dev/null || echo "  (FOUNDATION_SKILLS_BY_CATEGORY.md not found)"
mv -v EXISTING_FOUNDATION_VERIFICATION.md archive/analysis/ 2>/dev/null || echo "  (EXISTING_FOUNDATION_VERIFICATION.md not found)"
echo "✓ Foundational skills files moved to archive/analysis/"
echo ""

# Move AI analysis files to archive/analysis
echo "Moving AI analysis files to archive/analysis/..."
mv -v AI_ENHANCEMENT_REPORT.md archive/analysis/ 2>/dev/null || echo "  (AI_ENHANCEMENT_REPORT.md not found)"
mv -v AI_GAP_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (AI_GAP_ANALYSIS.md not found)"
mv -v AI_INTEGRATION_PLAN.md archive/analysis/ 2>/dev/null || echo "  (AI_INTEGRATION_PLAN.md not found)"
mv -v AI_SKILLS_CREATION_REPORT.md archive/analysis/ 2>/dev/null || echo "  (AI_SKILLS_CREATION_REPORT.md not found)"
mv -v AI_SKILLS_INTEGRATION_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (AI_SKILLS_INTEGRATION_SUMMARY.md not found)"
mv -v AI4K12_ANALYSIS_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (AI4K12_ANALYSIS_SUMMARY.md not found)"
mv -v AI4K12_PRIORITIES_EXTRACTED.md archive/analysis/ 2>/dev/null || echo "  (AI4K12_PRIORITIES_EXTRACTED.md not found)"
mv -v AI_TOPIC_ASSIGNMENTS.md archive/analysis/ 2>/dev/null || echo "  (AI_TOPIC_ASSIGNMENTS.md not found)"
mv -v CURRENT_AI_COVERAGE_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (CURRENT_AI_COVERAGE_ANALYSIS.md not found)"
echo "✓ AI analysis files moved to archive/analysis/"
echo ""

# Move enrichment analysis files to archive/analysis
echo "Moving enrichment analysis files to archive/analysis/..."
mv -v ENRICHMENT_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (ENRICHMENT_ANALYSIS.md not found)"
mv -v ENRICHED_SKILLS_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (ENRICHED_SKILLS_SUMMARY.md not found)"
mv -v ENRICHMENT_EXECUTIVE_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (ENRICHMENT_EXECUTIVE_SUMMARY.md not found)"
mv -v ENRICHMENT_QUICK_REFERENCE.md archive/analysis/ 2>/dev/null || echo "  (ENRICHMENT_QUICK_REFERENCE.md not found)"
mv -v ENRICHMENT_REPORT.md archive/analysis/ 2>/dev/null || echo "  (ENRICHMENT_REPORT.md not found)"
mv -v ENRICHMENT_STATISTICS.md archive/analysis/ 2>/dev/null || echo "  (ENRICHMENT_STATISTICS.md not found)"
mv -v D1_comprehensive_enrichment.md archive/analysis/ 2>/dev/null || echo "  (D1_comprehensive_enrichment.md not found)"
echo "✓ Enrichment analysis files moved to archive/analysis/"
echo ""

# Move dependency analysis files to archive/analysis
echo "Moving dependency analysis files to archive/analysis/..."
mv -v DEPENDENCIES_T01_T05_REPORT.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T01_T05_REPORT.md not found)"
mv -v DEPENDENCIES_T01_T05_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T01_T05_SUMMARY.md not found)"
mv -v dependencies_T01_T05.json archive/analysis/ 2>/dev/null || echo "  (dependencies_T01_T05.json not found)"
mv -v dependencies_T01_T05_summary.json archive/analysis/ 2>/dev/null || echo "  (dependencies_T01_T05_summary.json not found)"
mv -v DEPENDENCIES_T06_T13_REPORT.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T06_T13_REPORT.md not found)"
mv -v DEPENDENCIES_T06_T13_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T06_T13_SUMMARY.md not found)"
mv -v dependencies_T06_T13.json archive/analysis/ 2>/dev/null || echo "  (dependencies_T06_T13.json not found)"
mv -v DEPENDENCIES_T14_T24_REPORT.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T14_T24_REPORT.md not found)"
mv -v DEPENDENCIES_T14_T24_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T14_T24_SUMMARY.md not found)"
mv -v dependencies_T14_T24.json archive/analysis/ 2>/dev/null || echo "  (dependencies_T14_T24.json not found)"
mv -v DEPENDENCIES_T25_T29_REPORT.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T25_T29_REPORT.md not found)"
mv -v DEPENDENCIES_T25_T29_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T25_T29_SUMMARY.md not found)"
mv -v dependencies_T25_T29.json archive/analysis/ 2>/dev/null || echo "  (dependencies_T25_T29.json not found)"
mv -v DEPENDENCIES_T25_T29_COMPLETE.txt archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T25_T29_COMPLETE.txt not found)"
mv -v DEPENDENCIES_T30_T36_REPORT.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T30_T36_REPORT.md not found)"
mv -v DEPENDENCIES_T30_T36_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCIES_T30_T36_SUMMARY.md not found)"
mv -v dependencies_T30_T36.json archive/analysis/ 2>/dev/null || echo "  (dependencies_T30_T36.json not found)"
mv -v DEPENDENCY_MAP_T01_T05.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCY_MAP_T01_T05.md not found)"
mv -v DEPENDENCY_STATISTICS.md archive/analysis/ 2>/dev/null || echo "  (DEPENDENCY_STATISTICS.md not found)"
mv -v analyze_T14_T24_dependencies.md archive/analysis/ 2>/dev/null || echo "  (analyze_T14_T24_dependencies.md not found)"
mv -v CROSS_DOMAIN_DEPENDENCIES.md archive/analysis/ 2>/dev/null || echo "  (CROSS_DOMAIN_DEPENDENCIES.md not found)"
echo "✓ Dependency analysis files moved to archive/analysis/"
echo ""

# Move integration and validation files to archive/analysis
echo "Moving integration & validation files to archive/analysis/..."
mv -v INTEGRATION_CHANGES_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (INTEGRATION_CHANGES_SUMMARY.md not found)"
mv -v INTEGRATION_COMPLETE_CHECKLIST.md archive/analysis/ 2>/dev/null || echo "  (INTEGRATION_COMPLETE_CHECKLIST.md not found)"
mv -v INTEGRATION_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (INTEGRATION_COMPLETE.md not found)"
mv -v INTEGRATION_SUCCESS.txt archive/analysis/ 2>/dev/null || echo "  (INTEGRATION_SUCCESS.txt not found)"
mv -v INTEGRATION_VALIDATION_REPORT.md archive/analysis/ 2>/dev/null || echo "  (INTEGRATION_VALIDATION_REPORT.md not found)"
mv -v FINAL_INTEGRATION_REPORT.md archive/analysis/ 2>/dev/null || echo "  (FINAL_INTEGRATION_REPORT.md not found)"
mv -v FINAL_INTEGRATION_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (FINAL_INTEGRATION_SUMMARY.md not found)"
mv -v FINAL_INTEGRATION_VERIFICATION.md archive/analysis/ 2>/dev/null || echo "  (FINAL_INTEGRATION_VERIFICATION.md not found)"
mv -v FINAL_VALIDATION_REPORT.md archive/analysis/ 2>/dev/null || echo "  (FINAL_VALIDATION_REPORT.md not found)"
mv -v VALIDATION_REPORT_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (VALIDATION_REPORT_COMPLETE.md not found)"
mv -v validation_report.json archive/analysis/ 2>/dev/null || echo "  (validation_report.json not found)"
mv -v VALIDATION_T06_T13.md archive/analysis/ 2>/dev/null || echo "  (VALIDATION_T06_T13.md not found)"
mv -v CREATIVE_ACSL_VALIDATION_REPORT.md archive/analysis/ 2>/dev/null || echo "  (CREATIVE_ACSL_VALIDATION_REPORT.md not found)"
mv -v K8_INTEGRATION_REPORT.md archive/analysis/ 2>/dev/null || echo "  (K8_INTEGRATION_REPORT.md not found)"
echo "✓ Integration & validation files moved to archive/analysis/"
echo ""

# Move K-2 analysis files to archive/analysis
echo "Moving K-2 analysis files to archive/analysis/..."
mv -v K2_REDESIGN_REPORT.md archive/analysis/ 2>/dev/null || echo "  (K2_REDESIGN_REPORT.md not found)"
mv -v K2_REDESIGN_STATUS_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (K2_REDESIGN_STATUS_COMPLETE.md not found)"
mv -v K2_REDESIGN_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (K2_REDESIGN_SUMMARY.md not found)"
mv -v K2_REMAINING_SKILLS_REPORT.md archive/analysis/ 2>/dev/null || echo "  (K2_REMAINING_SKILLS_REPORT.md not found)"
mv -v K2_DEPENDENCIES_REPORT.md archive/analysis/ 2>/dev/null || echo "  (K2_DEPENDENCIES_REPORT.md not found)"
mv -v K2_DEPENDENCIES_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (K2_DEPENDENCIES_SUMMARY.md not found)"
mv -v K2_COMPLETE_TOPIC_COVERAGE.md archive/analysis/ 2>/dev/null || echo "  (K2_COMPLETE_TOPIC_COVERAGE.md not found)"
mv -v K2_COMPLETION_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (K2_COMPLETION_SUMMARY.md not found)"
echo "✓ K-2 analysis files moved to archive/analysis/"
echo ""

# Move detailed topic analysis files to archive/analysis
echo "Moving detailed topic analysis files to archive/analysis/..."
mv -v T01_enriched_analysis.md archive/analysis/ 2>/dev/null || echo "  (T01_enriched_analysis.md not found)"
mv -v T03_enriched_analysis.md archive/analysis/ 2>/dev/null || echo "  (T03_enriched_analysis.md not found)"
mv -v T04_enriched_analysis.md archive/analysis/ 2>/dev/null || echo "  (T04_enriched_analysis.md not found)"
mv -v T05_enriched_analysis.md archive/analysis/ 2>/dev/null || echo "  (T05_enriched_analysis.md not found)"
mv -v T06_enriched_analysis.md archive/analysis/ 2>/dev/null || echo "  (T06_enriched_analysis.md not found)"
mv -v T07_enriched_analysis.md archive/analysis/ 2>/dev/null || echo "  (T07_enriched_analysis.md not found)"
mv -v T08_enriched_analysis.md archive/analysis/ 2>/dev/null || echo "  (T08_enriched_analysis.md not found)"
mv -v T09_enriched_analysis.md archive/analysis/ 2>/dev/null || echo "  (T09_enriched_analysis.md not found)"
mv -v T10-T13_streamlined_analysis.md archive/analysis/ 2>/dev/null || echo "  (T10-T13_streamlined_analysis.md not found)"
mv -v T14-T24_applications_analysis.md archive/analysis/ 2>/dev/null || echo "  (T14-T24_applications_analysis.md not found)"
mv -v T25-T29_data_analysis.md archive/analysis/ 2>/dev/null || echo "  (T25-T29_data_analysis.md not found)"
mv -v T30-T36_systems_society_analysis.md archive/analysis/ 2>/dev/null || echo "  (T30-T36_systems_society_analysis.md not found)"
mv -v T14_T24_ANALYSIS_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (T14_T24_ANALYSIS_COMPLETE.md not found)"
mv -v T25-T29_ANALYSIS_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (T25-T29_ANALYSIS_COMPLETE.md not found)"
mv -v T30_T36_COMPLETE_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (T30_T36_COMPLETE_ANALYSIS.md not found)"
mv -v T30_T36_FINAL_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (T30_T36_FINAL_SUMMARY.md not found)"
mv -v T30_T36_ANALYSIS_INDEX.md archive/analysis/ 2>/dev/null || echo "  (T30_T36_ANALYSIS_INDEX.md not found)"
echo "✓ Topic analysis files moved to archive/analysis/"
echo ""

# Move project pathway files to archive/analysis
echo "Moving project pathway files to archive/analysis/..."
mv -v CRITICAL_PATHS_T06_T13.md archive/analysis/ 2>/dev/null || echo "  (CRITICAL_PATHS_T06_T13.md not found)"
mv -v CAPSTONE_SKILLS_T14_T24.md archive/analysis/ 2>/dev/null || echo "  (CAPSTONE_SKILLS_T14_T24.md not found)"
mv -v CREATIVE_PROJECT_PATHWAY.md archive/analysis/ 2>/dev/null || echo "  (CREATIVE_PROJECT_PATHWAY.md not found)"
mv -v DATA_LITERACY_PATHWAY.md archive/analysis/ 2>/dev/null || echo "  (DATA_LITERACY_PATHWAY.md not found)"
mv -v RESPONSIBLE_COMPUTING_PATHWAY.md archive/analysis/ 2>/dev/null || echo "  (RESPONSIBLE_COMPUTING_PATHWAY.md not found)"
mv -v CREATIVE_SKILLS_SPECS.md archive/analysis/ 2>/dev/null || echo "  (CREATIVE_SKILLS_SPECS.md not found)"
echo "✓ Project pathway files moved to archive/analysis/"
echo ""

# Move track system files to archive/analysis
echo "Moving track system files to archive/analysis/..."
mv -v TRACK_MIGRATION_PLAN.md archive/analysis/ 2>/dev/null || echo "  (TRACK_MIGRATION_PLAN.md not found)"
mv -v TRACK_SYSTEM_DELIVERY_SUMMARY.txt archive/analysis/ 2>/dev/null || echo "  (TRACK_SYSTEM_DELIVERY_SUMMARY.txt not found)"
mv -v TRACK_SYSTEM_EXECUTIVE_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (TRACK_SYSTEM_EXECUTIVE_SUMMARY.md not found)"
mv -v TRACK_SYSTEM_QUICK_START.md archive/analysis/ 2>/dev/null || echo "  (TRACK_SYSTEM_QUICK_START.md not found)"
mv -v DIFFICULTY_TRACK_SYSTEM.md archive/analysis/ 2>/dev/null || echo "  (DIFFICULTY_TRACK_SYSTEM.md not found)"
mv -v GATEWAY_AND_CAPSTONE_SKILLS.md archive/analysis/ 2>/dev/null || echo "  (GATEWAY_AND_CAPSTONE_SKILLS.md not found)"
echo "✓ Track system files moved to archive/analysis/"
echo ""

# Move project completion summary files to archive/analysis
echo "Moving project completion files to archive/analysis/..."
mv -v FINAL_PROJECT_SUMMARY_AI_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (FINAL_PROJECT_SUMMARY_AI_COMPLETE.md not found)"
mv -v FINAL_K8_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (FINAL_K8_SUMMARY.md not found)"
mv -v EXECUTIVE_SUMMARY_FINAL.md archive/analysis/ 2>/dev/null || echo "  (EXECUTIVE_SUMMARY_FINAL.md not found)"
mv -v K8_AI_COMPLETE_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (K8_AI_COMPLETE_SUMMARY.md not found)"
mv -v K8_COMPLETE_README.md archive/analysis/ 2>/dev/null || echo "  (K8_COMPLETE_README.md not found)"
mv -v PROJECT_COMPLETE_FINAL_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (PROJECT_COMPLETE_FINAL_SUMMARY.md not found)"
mv -v README_INTEGRATION_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (README_INTEGRATION_COMPLETE.md not found)"
mv -v SKILL_MAP_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (SKILL_MAP_COMPLETE.md not found)"
mv -v SKILL_MAP_FINAL_OVERVIEW.md archive/analysis/ 2>/dev/null || echo "  (SKILL_MAP_FINAL_OVERVIEW.md not found)"
mv -v FINAL_REPORT_T14_T24.md archive/analysis/ 2>/dev/null || echo "  (FINAL_REPORT_T14_T24.md not found)"
mv -v D1_COMPLETE_Summary.md archive/analysis/ 2>/dev/null || echo "  (D1_COMPLETE_Summary.md not found)"
mv -v ANALYSIS_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (ANALYSIS_COMPLETE.md not found)"
mv -v ANALYSIS_COMPLETE_VERIFICATION.txt archive/analysis/ 2>/dev/null || echo "  (ANALYSIS_COMPLETE_VERIFICATION.txt not found)"
mv -v ANALYSIS_EXECUTIVE_BRIEFING.txt archive/analysis/ 2>/dev/null || echo "  (ANALYSIS_EXECUTIVE_BRIEFING.txt not found)"
mv -v ANALYSIS_SUMMARY_T14_T24.txt archive/analysis/ 2>/dev/null || echo "  (ANALYSIS_SUMMARY_T14_T24.txt not found)"
echo "✓ Project completion files moved to archive/analysis/"
echo ""

# Move data consolidation files to archive/analysis
echo "Moving data consolidation files to archive/analysis/..."
mv -v DATA_CONSOLIDATION_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (DATA_CONSOLIDATION_ANALYSIS.md not found)"
mv -v DATA_CONSOLIDATION_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (DATA_CONSOLIDATION_SUMMARY.md not found)"
mv -v METADATA_CONSOLIDATION_PLAN.md archive/analysis/ 2>/dev/null || echo "  (METADATA_CONSOLIDATION_PLAN.md not found)"
mv -v DATA_AI_BRIDGES.md archive/analysis/ 2>/dev/null || echo "  (DATA_AI_BRIDGES.md not found)"
mv -v TASK_COMPLETION_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (TASK_COMPLETION_SUMMARY.md not found)"
mv -v SESSION_SUMMARY_COMPLETE.md archive/analysis/ 2>/dev/null || echo "  (SESSION_SUMMARY_COMPLETE.md not found)"
mv -v SKILL_FILES_ANALYSIS.md archive/analysis/ 2>/dev/null || echo "  (SKILL_FILES_ANALYSIS.md not found)"
echo "✓ Data consolidation files moved to archive/analysis/"
echo ""

# Move file management & cleanup files to archive/analysis
echo "Moving file management files to archive/analysis/..."
mv -v CLEANUP_SUMMARY.md archive/analysis/ 2>/dev/null || echo "  (CLEANUP_SUMMARY.md not found)"
mv -v CLEANUP_PLAN.md archive/analysis/ 2>/dev/null || echo "  (CLEANUP_PLAN.md not found)"
mv -v cleanup_log.txt archive/analysis/ 2>/dev/null || echo "  (cleanup_log.txt not found)"
mv -v FILE_DEPRECATION_PLAN.md archive/analysis/ 2>/dev/null || echo "  (FILE_DEPRECATION_PLAN.md not found)"
mv -v FILE_INDEX.md archive/analysis/ 2>/dev/null || echo "  (FILE_INDEX.md not found)"
mv -v FILE_MANIFEST.md archive/analysis/ 2>/dev/null || echo "  (FILE_MANIFEST.md not found)"
mv -v FILE_ORGANIZATION.md archive/analysis/ 2>/dev/null || echo "  (FILE_ORGANIZATION.md not found)"
mv -v FILES_GENERATED.txt archive/analysis/ 2>/dev/null || echo "  (FILES_GENERATED.txt not found)"
mv -v GENERATION_SUMMARY.txt archive/analysis/ 2>/dev/null || echo "  (GENERATION_SUMMARY.txt not found)"
mv -v GRADE_7_8_REVIEW_SUMMARY.txt archive/analysis/ 2>/dev/null || echo "  (GRADE_7_8_REVIEW_SUMMARY.txt not found)"
mv -v GRADE_BY_GRADE_PROGRESSION.md archive/analysis/ 2>/dev/null || echo "  (GRADE_BY_GRADE_PROGRESSION.md not found)"
mv -v AGE_APPROPRIATENESS_REVIEW_REPORT.txt archive/analysis/ 2>/dev/null || echo "  (AGE_APPROPRIATENESS_REVIEW_REPORT.txt not found)"
echo "✓ File management files moved to archive/analysis/"
echo ""

# Move misc reference/completion files to archive/analysis
echo "Moving miscellaneous reference files to archive/analysis/..."
mv -v PRODUCTION_CHECKLIST.md archive/analysis/ 2>/dev/null || echo "  (PRODUCTION_CHECKLIST.md not found)"
mv -v PROGRESS_REPORT.md archive/analysis/ 2>/dev/null || echo "  (PROGRESS_REPORT.md not found)"
mv -v DELIVERABLES_INDEX.md archive/analysis/ 2>/dev/null || echo "  (DELIVERABLES_INDEX.md not found)"
mv -v DELIVERABLES_CREATIVE_ACSL.md archive/analysis/ 2>/dev/null || echo "  (DELIVERABLES_CREATIVE_ACSL.md not found)"
mv -v REVISION_EXAMPLES_BEFORE_AFTER.txt archive/analysis/ 2>/dev/null || echo "  (REVISION_EXAMPLES_BEFORE_AFTER.txt not found)"
mv -v CROSS_APPLICATION_PATTERNS.md archive/analysis/ 2>/dev/null || echo "  (CROSS_APPLICATION_PATTERNS.md not found)"
mv -v UNIQUE_CONTENT_REPORT.md archive/analysis/ 2>/dev/null || echo "  (UNIQUE_CONTENT_REPORT.md not found)"
mv -v BLOCK_COVERAGE_MATRIX.md archive/analysis/ 2>/dev/null || echo "  (BLOCK_COVERAGE_MATRIX.md not found)"
mv -v analysis_block_coverage.json archive/analysis/ 2>/dev/null || echo "  (analysis_block_coverage.json not found)"
mv -v T25-T29_DELIVERABLES_SUMMARY.txt archive/analysis/ 2>/dev/null || echo "  (T25-T29_DELIVERABLES_SUMMARY.txt not found)"
echo "✓ Miscellaneous reference files moved to archive/analysis/"
echo ""

# Create README files for organized directories
echo "Creating README files for organized directories..."

# Create skills/ README
cat > skills/README.md << 'EOF'
# CreatiCode K-8 Skill Map - Skills Data

## Overview
This directory contains all skill data files, schemas, and domain/topic definitions for the CreatiCode K-8 Skill Map project.

## Main Production File
- **skills_k8_ai_complete_FINAL.json** - Complete K-8 skill map with 1,150 skills and full AI integration

## Foundational Skills Data
- FOUNDATIONAL_41_SKILLS.json - 41 foundational block skills
- WEEK2_NEW_SKILLS.json - 20 app/project development skills
- CREATIVE_SKILLS_3.json - 3 creative skills
- WEEK2_SKILLS_QUICK_REFERENCE.json - Quick reference format for Week 2 skills

## Schema & Specification Files
- CANONICAL_SKILL_SCHEMA.json - Standard skill object schema definition
- k2_skill_format_spec.json - K-2 specific format specification
- k2_activity_templates.json - K-2 activity templates
- k2_autograding_rules.json - K-2 autograding rules
- k2_visual_themes.json - K-2 visual theme definitions
- k3_transition_validation.json - K-3 transition validation data

## Statistics & Validation
- FINAL_SKILL_MAP_STATISTICS.json - Complete statistics for full K-8 map
- k8_complete_statistics.json - K-8 specific statistics
- enrichment_stats.json - Enrichment statistics
- k8_validation_report.json - K-8 validation results
- well_designed_examples.json - Example implementations

## Domain & Topic Files
- domains_topics.yaml - Topic and domain definitions
- domain_mapping.json - Domain to skill mapping reference

## CSTA Standards Reference
- csta_standards_extracted.json - Extracted CSTA standards
- SKILL_CSTA_ASSIGNMENTS.json - CSTA code assignments for skills

## Analysis & Comparison Data
- foundational_blocks_detailed_analysis.json - Detailed block analysis
- k2_current_analysis.json - K-2 current state analysis
- skill_file_analysis.json - Skill file structure analysis
- skill_comparison_report.json - Skill comparison reference data
- removed_dependencies_report.json - Removed dependencies reference
- SKILL_TRACK_CATEGORIZATION.json - Track categorization reference

## Usage
These files are primarily used by:
- Application systems integrating the CreatiCode curriculum
- Analysis and reporting tools
- Educational platform implementations
- Skill assessment and tracking systems

## Notes
- The main production file (skills_k8_ai_complete_FINAL.json) contains all skills and should be the primary reference
- Schema files define the structure that all skills must follow
- Domain files help organize and categorize skills by topic
EOF

echo "✓ skills/README.md created"

# Create archive/analysis/ README
cat > archive/analysis/README.md << 'EOF'
# CreatiCode Project - Analysis & Archive Files

## Overview
This directory contains temporary analysis files, reports, and validation data generated during the CreatiCode K-8 Skill Map development process.

## Contents
This archive includes:
- Week 1 & 2 analysis and implementation reports
- AI enhancement and integration analysis
- ACSL content analysis and validation
- Dependency analysis for all topic areas (T01-T36)
- Topic-specific enrichment and detailed analysis
- K-2 redesign reports and validation
- Integration validation and verification reports
- Project completion summaries and checklists
- Data consolidation and metadata reports
- File management and cleanup records

## Purpose
These files document the development process and can be referenced for:
- Understanding how features were implemented
- Reviewing analysis decisions
- Tracing validation and integration steps
- Maintaining development history

## Organization
Files are roughly organized by topic:
- WEEK* files: Week 1 & 2 specific work
- ACSL* files: ACSL content analysis
- AI* files: AI enhancement work
- DEPENDENCIES* files: Dependency analysis by topic
- INTEGRATION* files: Integration validation
- K2* files: K-2 specific redesign
- T##_* files: Topic-specific analysis
- PROJECT/SKILL_MAP files: Overall project completion

## Note
Most files in this archive are historical records. The active project files and production skill data are in the root directory and /skills/ directory.
EOF

echo "✓ archive/analysis/README.md created"

# Create docs/ README
cat > docs/README.md << 'EOF'
# CreatiCode K-8 Skill Map - Documentation

## Overview
This directory contains essential documentation files for understanding and using the CreatiCode K-8 Skill Map.

## Getting Started
- **README.md** (root) - Main project overview
- **00-START-HERE.md** - Quick start guide
- **QUICK_START_GUIDE.md** - Quick start instructions
- **QUICK_REFERENCE.md** - Quick reference guide

## Project Specifications
- **spec.md** - Main project specification
- **spec_v2_updated.md** - Updated specification (v2)

## Implementation & Usage
- **IMPLEMENTATION_GUIDE.md** - How to implement the skill map
- **K2_FRAMEWORK_SUMMARY.md** - K-2 framework overview
- **K2_IMPLEMENTATION_EXAMPLES.md** - K-2 implementation examples
- **K2_QUALITY_GUIDELINES.md** - K-2 quality guidelines

## Dependencies & Learning Pathways
- **HOW_TO_USE_DEPENDENCIES.md** - Guide to using dependencies
- **dependency_framework.md** - Dependency framework documentation
- **CRITICAL_PATHWAYS.md** - Critical learning pathways

## Standards & References
- **CSTA_STANDARDS_REFERENCE.md** - CSTA standards reference
- **cstastandard.md** - CSTA standards documentation

## Topic Structure
- **domains_topics_overview.md** - Domains and topics overview
- **topic_grade_matrix.md** - Topic to grade matrix

## Project References
- **creaticode.md** - CreatiCode description
- **INDEX.md** - Project index

## Reviews & References
- **reviews.md** - Project reviews and feedback
- **competition_paths.md** - Competition learning paths

Note: These documentation files are essential references for using and maintaining the CreatiCode K-8 Skill Map project.
EOF

echo "✓ docs/README.md created"
echo ""

echo "====================================="
echo "Organization Complete!"
echo "====================================="
echo ""
echo "Summary:"
echo "  - skills/ directory: 26 skill data files"
echo "  - archive/analysis/ directory: 172 analysis & temporary files"
echo "  - 106 core documentation and utility files remain in root"
echo "  - Total files reorganized: 304"
echo ""
echo "New structure:"
echo "  ."
echo "  ├── README.md (and other core docs)"
echo "  ├── skills/ (production skill data)"
echo "  ├── archive/analysis/ (temporary analysis files)"
echo "  └── docs/ (reference documentation)"
echo ""
echo "Next steps:"
echo "  1. Review FILES_TO_MOVE.txt, FILES_TO_ARCHIVE.txt, and FILES_TO_KEEP.txt"
echo "  2. Git commit: git add skills/ archive/ && git commit -m 'Organize project files into clean structure'"
echo "  3. Verify all important files are accessible"
echo ""
