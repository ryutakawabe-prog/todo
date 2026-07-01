# 🏷️ ラベル管理ガイド

## 📌 優先度ラベル

Issue の優先度を示すラベルです。各 Issue に **1 つだけ** 付けてください。

### 優先度レベル

| ラベル | 色 | 説明 | 対応時期 |
|--------|------|------|---------|
| `priority:high` | 🔴 赤 | 高優先度 - 即座に対応が必要 | 今すぐ |
| `priority:medium` | 🟠 オレンジ | 中優先度 - スプリント内に対応 | このスプリント中 |
| `priority:low` | 🟢 緑 | 低優先度 - 次スプリント以降で OK | 余裕があれば |

---

## 📋 ステータスラベル

Issue の進行状況を示します。

| ラベル | 色 | 説明 |
|--------|------|------|
| `status:todo` | ⚫ グレー | 未着手 |
| `status:in-progress` | 🟡 黄 | 進行中 |
| `status:review` | 🔵 薄青 | レビュー待ち |
| `status:done` | 🟢 緑 | 完了 |

---

## 🎯 タイプラベル

Issue の種類を示します。

| ラベル | 色 | 説明 |
|--------|------|------|
| `type:feature` | 🔷 濃青 | 新機能 |
| `type:bug` | 🔴 赤 | バグ修正 |
| `type:improvement` | 🟣 紫 | 改善・リファクタ |
| `type:documentation` | 🟢 緑 | ドキュメント |

---

## 🏃 スプリントラベル

所属するスプリントを示します。

| ラベル | 説明 |
|--------|------|
| `sprint-1` ~ `sprint-12` | Sprint 1 ～ 12 |

---

## 💡 使い方の例

### 例 1: 高優先度の新機能
```
Title: [FEATURE] ユーザー認証機能を実装

Labels:
  - priority:high ← 優先度
  - type:feature ← 種類
  - sprint-1 ← スプリント
  - status:todo ← ステータス
```

### 例 2: 低優先度のバグ修正
```
Title: [BUG] ログイン画面のレイアウト崩れ

Labels:
  - priority:low
  - type:bug
  - sprint-2
  - status:in-progress
```

---

## ⚙️ ラベル付けの手順

### 1️⃣ Issue を作成
👉 https://github.com/ryutakawabe-prog/todo/issues/new

### 2️⃣ ラベルを付ける
- Issue の右側にある **Labels** セクションをクリック
- 優先度・タイプ・スプリント・ステータスのラベルを選択

### 3️⃣ 保存
変更は自動保存されます ✅

---

## 🔍 ラベル一覧を見る

👉 https://github.com/ryutakawabe-prog/todo/labels

ここからラベルを作成・編集できます。

---

**次は Issue を作成してラベルを試してみてください！** 🚀
