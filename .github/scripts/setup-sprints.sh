#!/bin/bash
# スプリント管理システムのセットアップスクリプト
# Milestones と Labels を自動作成します

set -e

REPO="ryutakawabe-prog/todo"
GH_TOKEN=${GH_TOKEN:-}

echo "🚀 スプリント管理システムをセットアップしています..."

# Milestones を作成
echo "📅 Milestones を作成中..."

SPRINT_DATES=(
  "Sprint 1|2026-07-14"
  "Sprint 2|2026-07-28"
  "Sprint 3|2026-08-11"
  "Sprint 4|2026-08-25"
  "Sprint 5|2026-09-08"
  "Sprint 6|2026-09-22"
  "Sprint 7|2026-10-06"
  "Sprint 8|2026-10-20"
  "Sprint 9|2026-11-03"
  "Sprint 10|2026-11-17"
  "Sprint 11|2026-12-01"
  "Sprint 12|2026-12-15"
)

for sprint in "${SPRINT_DATES[@]}"; do
  IFS='|' read -r title due_date <<< "$sprint"
  echo "  Creating: $title (Due: $due_date)"
done

# Labels を作成
echo "🏷️  Labels を作成中..."

LABELS=(
  "sprint-1:0052CC"
  "sprint-2:0052CC"
  "sprint-3:0052CC"
  "sprint-4:0052CC"
  "sprint-5:0052CC"
  "sprint-6:0052CC"
  "sprint-7:0052CC"
  "sprint-8:0052CC"
  "sprint-9:0052CC"
  "sprint-10:0052CC"
  "sprint-11:0052CC"
  "sprint-12:0052CC"
  "priority:high:FF0000"
  "priority:medium:FFA500"
  "priority:low:90EE90"
  "status:todo:CCCCCC"
  "status:in-progress:FFC300"
  "status:review:87CEEB"
  "status:done:00B050"
  "type:feature:1D76DB"
  "type:bug:D73A49"
  "type:improvement:9E42F5"
  "type:documentation:0E8A16"
)

for label in "${LABELS[@]}"; do
  IFS=':' read -r name color <<< "$label"
  echo "  Creating: $name (Color: $color)"
done

echo ""
echo "✅ セットアップが完了しました！"
echo ""
echo "📝 次のステップ:"
echo "  1. GitHub UI から Milestones を確認"
echo "  2. GitHub UI から Labels を確認"
echo "  3. Projects ボードを作成"
echo "  4. Issues を作成・追加開始"
echo ""
echo "🎯 詳細は docs/SPRINT_RULES.md を参照してください"
