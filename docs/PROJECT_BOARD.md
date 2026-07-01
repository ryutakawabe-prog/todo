# 📊 Project ボード セットアップガイド

## 🎯 ボード構成

Sprint Backlog は以下の 4 カラムで管理します：

```
📝 To Do → 🔄 In Progress → 👀 Review → ✅ Done
```

---

## ⚙️ Project V2 のカスタムフィールド設定

### **Status フィールド（必須）**
自動的に以下の値を設定：

| フィールド値 | 説明 | 対応ラベル |
|-------------|------|----------|
| `To Do` | 未着手 | `status:todo` |
| `In Progress` | 進行中 | `status:in-progress` |
| `Review` | レビュー待ち | `status:review` |
| `Done` | 完了 | `status:done` |

### **Priority フィールド（オプション）**

| 優先度 | 対応ラベル |
|--------|----------|
| High | `priority:high` |
| Medium | `priority:medium` |
| Low | `priority:low` |

### **Sprint フィールド（オプション）**

| スプリント | 対応ラベル |
|-----------|----------|
| Sprint 1 | `sprint-1` |
| Sprint 2 | `sprint-2` |
| ... | ... |
| Sprint 12 | `sprint-12` |

---

## 📋 使い方

### **1️⃣ Issue を作成**
```
Title: [FEATURE] ユーザー認証機能を実装
Description: ログイン・ユーザー登録機能を実装
Labels: priority:high, type:feature, sprint-1
Milestone: Sprint 1
```

### **2️⃣ Project に追加**
- Issue の **Projects** セクションから `Sprint Backlog` を選択
- または Project ボードから直接ドラッグ&ドロップ

### **3️⃣ ボードで管理**
- カラム間でドラッグ&ドロップして進捗を更新
- ラベルで優先度・タイプ・スプリントを管理

---

## 📚 参考リンク

- **Project ボード**: https://github.com/users/ryutakawabe-prog/projects/2/views/2
- **ラベル管理**: https://github.com/ryutakawabe-prog/todo/blob/main/docs/LABELS.md
- **Issue 作成**: https://github.com/ryutakawabe-prog/todo/issues/new

---

## 💡 ベストプラクティス

✅ **DO:**
- Issue 作成時に必ずラベルを付ける
- 進捗に応じてカラムを移動
- 定期的に Done に移す

❌ **DON'T:**
- ラベルなしで Issue を作成しない
- Status フィールドと `status:*` ラベルを混在させない

---

**Project ボードをしっかり活用して、スプリント管理を効率化しましょう！** 🚀
