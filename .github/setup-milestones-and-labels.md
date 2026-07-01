# スプリント管理システム セットアップガイド

⚠️ **重要**: GitHub API では Milestones と Labels の一括作成ができないため、以下の手順で手動作成してください。

---

## 📅 Milestones 作成手順

### 作成方法
1. リポジトリを開く: https://github.com/ryutakawabe-prog/todo
2. **Issues** タブ → **Milestones**
3. **New Milestone** をクリック
4. 以下を参考に作成

### 作成するミルストーン一覧

| Milestone | Due Date |
|-----------|----------|
| Sprint 1 | 2026-07-14 |
| Sprint 2 | 2026-07-28 |
| Sprint 3 | 2026-08-11 |
| Sprint 4 | 2026-08-25 |
| Sprint 5 | 2026-09-08 |
| Sprint 6 | 2026-09-22 |
| Sprint 7 | 2026-10-06 |
| Sprint 8 | 2026-10-20 |
| Sprint 9 | 2026-11-03 |
| Sprint 10 | 2026-11-17 |
| Sprint 11 | 2026-12-01 |
| Sprint 12 | 2026-12-15 |

---

## 🏷️ Labels 作成手順

### 作成方法
1. リポジトリを開く: https://github.com/ryutakawabe-prog/todo
2. **Issues** タブ → **Labels**
3. **New Label** をクリック
4. 以下を参考に作成

### スプリントラベル
```
sprint-1 (Color: #0052CC - Blue)
sprint-2 (Color: #0052CC - Blue)
sprint-3 (Color: #0052CC - Blue)
sprint-4 (Color: #0052CC - Blue)
sprint-5 (Color: #0052CC - Blue)
sprint-6 (Color: #0052CC - Blue)
sprint-7 (Color: #0052CC - Blue)
sprint-8 (Color: #0052CC - Blue)
sprint-9 (Color: #0052CC - Blue)
sprint-10 (Color: #0052CC - Blue)
sprint-11 (Color: #0052CC - Blue)
sprint-12 (Color: #0052CC - Blue)
```

### 優先度ラベル
```
priority:high (Color: #FF0000 - Red)
priority:medium (Color: #FFA500 - Orange)
priority:low (Color: #90EE90 - Light Green)
```

### ステータスラベル
```
status:todo (Color: #CCCCCC - Gray)
status:in-progress (Color: #FFC300 - Yellow)
status:review (Color: #87CEEB - Light Blue)
status:done (Color: #00B050 - Green)
```

### タイプラベル
```
type:feature (Color: #1D76DB - Dark Blue)
type:bug (Color: #D73A49 - Red)
type:improvement (Color: #9E42F5 - Purple)
type:documentation (Color: #0E8A16 - Green)
```

---

## 🎯 Projects ボード作成（推奨）

### 作成方法
1. リポジトリを開く: https://github.com/ryutakawabe-prog/todo
2. **Projects** タブ
3. **New Project** をクリック
4. プロジェクト名: `Sprint Backlog`
5. 説明: `スプリントバックログの Kanban ボード`
6. テンプレート: **Board** を選択

### ボードのカラム設定

作成後、デフォルトカラムを以下のように変更：

```
📝 To Do        → タスク未着手
🔄 In Progress  → 進行中タスク
👀 In Review    → レビュー待ちタスク
✅ Done         → 完了タスク
```

### ボード活用方法

1. 各 Issue を **Board** に追加
2. `status:in-progress` ラベルをつけたら **In Progress** へドラッグ
3. PR がマージされたら `status:done` へ移動
4. 日々 Board を確認して進捗管理

---

## 📝 Issue 作成開始

セットアップ完了後、以下の形式で Issue を作成：

### タイトル例
```
[FEATURE] ユーザー登録機能を実装する (SP: 5)
[BUG] ログイン画面で エラーが表示される (SP: 3)
[IMPROVEMENT] レスポンス時間を改善する (SP: 8)
```

### 必須ラベル
- `sprint-X` - どのスプリントか
- `priority:X` - 優先度
- `type:X` - タイプ

### 推奨設定
- **Milestone**: Sprint X を選択
- **Assignee**: 担当者を割り当て
- **Description**: 詳細説明、受け入れ基準を記載

---

## ✅ セットアップ完了チェックリスト

- [ ] 12個の Milestones を作成
- [ ] 23個の Labels を作成
- [ ] Projects ボードを作成
- [ ] Issue テンプレートが動作確認済み
- [ ] README.md と SPRINT_RULES.md を確認
- [ ] 最初の Issue を作成テスト

---

## 🚀 使い始める！

すべて準備完了したら、最初の Issue を作成して Projects ボードに追加しましょう！

**Happy Sprinting! 🎯**
