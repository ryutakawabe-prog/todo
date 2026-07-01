#!/usr/bin/env python3
"""
スプリント管理システムの自動セットアップスクリプト
Milestones と Labels を一括作成します
"""

import subprocess
import json
import sys
from datetime import datetime, timedelta

# リポジトリ情報
REPO_OWNER = "ryutakawabe-prog"
REPO_NAME = "todo"
REPO = f"{REPO_OWNER}/{REPO_NAME}"

# Milestones 定義
MILESTONES = [
    {"title": "Sprint 1", "due_date": "2026-07-14"},
    {"title": "Sprint 2", "due_date": "2026-07-28"},
    {"title": "Sprint 3", "due_date": "2026-08-11"},
    {"title": "Sprint 4", "due_date": "2026-08-25"},
    {"title": "Sprint 5", "due_date": "2026-09-08"},
    {"title": "Sprint 6", "due_date": "2026-09-22"},
    {"title": "Sprint 7", "due_date": "2026-10-06"},
    {"title": "Sprint 8", "due_date": "2026-10-20"},
    {"title": "Sprint 9", "due_date": "2026-11-03"},
    {"title": "Sprint 10", "due_date": "2026-11-17"},
    {"title": "Sprint 11", "due_date": "2026-12-01"},
    {"title": "Sprint 12", "due_date": "2026-12-15"},
]

# Labels 定義
LABELS = [
    # スプリントラベル
    {"name": "sprint-1", "color": "0052CC", "description": "Sprint 1"},
    {"name": "sprint-2", "color": "0052CC", "description": "Sprint 2"},
    {"name": "sprint-3", "color": "0052CC", "description": "Sprint 3"},
    {"name": "sprint-4", "color": "0052CC", "description": "Sprint 4"},
    {"name": "sprint-5", "color": "0052CC", "description": "Sprint 5"},
    {"name": "sprint-6", "color": "0052CC", "description": "Sprint 6"},
    {"name": "sprint-7", "color": "0052CC", "description": "Sprint 7"},
    {"name": "sprint-8", "color": "0052CC", "description": "Sprint 8"},
    {"name": "sprint-9", "color": "0052CC", "description": "Sprint 9"},
    {"name": "sprint-10", "color": "0052CC", "description": "Sprint 10"},
    {"name": "sprint-11", "color": "0052CC", "description": "Sprint 11"},
    {"name": "sprint-12", "color": "0052CC", "description": "Sprint 12"},
    # 優先度ラベル
    {"name": "priority:high", "color": "FF0000", "description": "高優先度 - 即座に対応が必要"},
    {"name": "priority:medium", "color": "FFA500", "description": "中優先度 - スプリント内に対応"},
    {"name": "priority:low", "color": "90EE90", "description": "低優先度 - 次スプリント以降で OK"},
    # ステータスラベル
    {"name": "status:todo", "color": "CCCCCC", "description": "未着手"},
    {"name": "status:in-progress", "color": "FFC300", "description": "進行中"},
    {"name": "status:review", "color": "87CEEB", "description": "レビュー待ち"},
    {"name": "status:done", "color": "00B050", "description": "完了"},
    # タイプラベル
    {"name": "type:feature", "color": "1D76DB", "description": "新機能"},
    {"name": "type:bug", "color": "D73A49", "description": "バグ修正"},
    {"name": "type:improvement", "color": "9E42F5", "description": "改善・リファクタ"},
    {"name": "type:documentation", "color": "0E8A16", "description": "ドキュメント"},
]


def run_gh_command(args):
    """GitHub CLI コマンドを実行"""
    try:
        result = subprocess.run(
            ["gh"] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout, result.returncode
    except subprocess.CalledProcessError as e:
        print(f"❌ エラー: {e.stderr}")
        return None, e.returncode
    except FileNotFoundError:
        print("❌ エラー: GitHub CLI (gh) がインストールされていません")
        print("👉 インストール: https://cli.github.com/")
        sys.exit(1)


def create_milestones():
    """Milestones を作成"""
    print("\n📅 Milestones を作成中...\n")
    created = 0
    
    for milestone in MILESTONES:
        print(f"  Creating: {milestone['title']} (Due: {milestone['due_date']})")
        
        args = [
            "api", "repos", REPO_OWNER, REPO_NAME, "milestones",
            "-X", "POST",
            "-f", f"title={milestone['title']}",
            "-f", f"due_on={milestone['due_date']}T23:59:59Z",
        ]
        
        output, code = run_gh_command(args)
        
        if code == 0:
            print(f"    ✅ 作成完了\n")
            created += 1
        else:
            print(f"    ⚠️  作成失敗\n")
    
    print(f"✅ {created}/{len(MILESTONES)} 個の Milestones を作成しました\n")
    return created


def create_labels():
    """Labels を作成"""
    print("\n🏷️  Labels を作成中...\n")
    created = 0
    
    for label in LABELS:
        print(f"  Creating: {label['name']} (Color: {label['color']})")
        
        args = [
            "api", "repos", REPO_OWNER, REPO_NAME, "labels",
            "-X", "POST",
            "-f", f"name={label['name']}",
            "-f", f"color={label['color']}",
            "-f", f"description={label['description']}",
        ]
        
        output, code = run_gh_command(args)
        
        if code == 0:
            print(f"    ✅ 作成完了\n")
            created += 1
        else:
            print(f"    ⚠️  作成失敗\n")
    
    print(f"✅ {created}/{len(LABELS)} 個の Labels を作成しました\n")
    return created


def main():
    """メイン処理"""
    print("=" * 60)
    print("🚀 スプリント管理システム セットアップ")
    print("=" * 60)
    print(f"\n📦 リポジトリ: {REPO}")
    print(f"📅 Milestones: {len(MILESTONES)} 個")
    print(f"🏷️  Labels: {len(LABELS)} 個")
    
    # 確認
    response = input("\n本当に作成しますか？ (y/n): ")
    if response.lower() != 'y':
        print("❌ キャンセルしました")
        sys.exit(0)
    
    # Milestones 作成
    milestone_count = create_milestones()
    
    # Labels 作成
    label_count = create_labels()
    
    # 結果表示
    print("=" * 60)
    print("✅ セットアップが完了しました！")
    print("=" * 60)
    print(f"\n📊 作成結果:")
    print(f"  📅 Milestones: {milestone_count}/{len(MILESTONES)}")
    print(f"  🏷️  Labels: {label_count}/{len(LABELS)}")
    print(f"\n📋 次のステップ:")
    print(f"  1. https://github.com/{REPO}/projects を開く")
    print(f"  2. New Project で 'Sprint Backlog' を作成")
    print(f"  3. Issues を作成してボードに追加")
    print(f"\n🎯 詳細: docs/SPRINT_RULES.md を参照\n")


if __name__ == "__main__":
    main()
