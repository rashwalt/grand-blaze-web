# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings


# ルート
urlpatterns = patterns(
    'website.views.root',
    
    # トップページ
    url(r'^$', 'index', name='root_index'),
    
    # インフォメーション
    url(r'^information/$', 'information', name='root_information'),
    
    # お知らせカテゴリ一覧
    url(r'^information/list/(?P<category_id>[0-4])/$', 'category', name='root_category'),
    url(r'^information/list/(?P<category_id>[0-4])/(?P<page>\d+)/$', 'category', name='root_category'),
    
    # お知らせ詳細
    url(r'^information/view/(?P<notice_id>\d+)/$', 'notice_detail', name='root_notice_detail'),
    
    # お問い合わせ
    url(r'^support/$', 'support_index', name='root_support_index'),
    
    # お問い合わせ完了
    url(r'^support/done/$', 'support_done', name='root_support_done'),
    
    # キャッシュクリア
    url(r'^cache_clear/$', 'cache_clear', name='root_cache_clear'),
    
)

# シンプル
urlpatterns += patterns(
    'django.views.generic.simple',
    
    # root
    
    # Grand Blazeの世界
    url(r'^startup/$', 'direct_to_template', {'template': 'root/startup.html'}, name='root_startup'),
    
    # FAQ
    url(r'^faq/$', 'direct_to_template', {'template': 'root/faq.html'}, name='root_faq'),
    
    # このサイトについて
    url(r'^about/$', 'direct_to_template', {'template': 'root/about.html'}, name='root_about'),
    
    # アイデア投稿
    url(r'^support/idea/$', 'direct_to_template', {'template': 'root/idea.html'}, name='root_idea'),
    
    # サイト内検索
    url(r'^search/$', 'direct_to_template', {'template': 'root/search.html'}, name='root_search'),
    
    # forum
    
    # フォーラムガイドライン
    url(r'^forum/guideline/$', 'direct_to_template', {'template': 'forum/guideline.html'}, name='forum_guideline'),
    
    # playgude
    
    # プレイガイド
    url(r'^playguide/$', 'direct_to_template', {'template': 'playguide/guide_index.html'}, name='playguide_index'),
    
    # プレイガイドの見かた
    url(r'^playguide/about/$', 'direct_to_template', {'template': 'playguide/about.html'}, name='playguide_about'),
    
    # プレイ上のお願い
    url(r'^playguide/caution/$', 'direct_to_template', {'template': 'playguide/caution.html'}, name='playguide_caution'),
    
    # Grand Blaze会員規約
    url(r'^playguide/testplayer_rules/$', 'direct_to_template', {'template': 'playguide/testplayer_rules.html'}, name='playguide_testplayer_rules'),
    
    # 新規登録の流れ
    url(r'^playguide/start_chart/$', 'direct_to_template', {'template': 'playguide/start_chart.html'}, name='playguide_start_chart'),
    
    # 新規登録について
    url(r'^playguide/newgame/$', 'direct_to_template', {'template': 'playguide/newgame.html'}, name='playguide_newgame'),
    
    # 冒険（処理）の流れ
    url(r'^playguide/flowchart/$', 'direct_to_template', {'template': 'playguide/flowchart.html'}, name='playguide_flowchart'),
    
    # 継続登録の提出
    url(r'^playguide/continue/$', 'direct_to_template', {'template': 'playguide/continue.html'}, name='playguide_continue'),
    
    # 移動先の決定
    url(r'^playguide/moving/$', 'direct_to_template', {'template': 'playguide/moving.html'}, name='playguide_moving'),
    
    # パーティの編成
    url(r'^playguide/party/$', 'direct_to_template', {'template': 'playguide/party.html'}, name='playguide_party'),
    
    # アイテムの使用
    url(r'^playguide/using_item/$', 'direct_to_template', {'template': 'playguide/using_item.html'}, name='playguide_using_item'),
    
    # プライベートスキル
    url(r'^playguide/private_skill/$', 'direct_to_template', {'template': 'playguide/private_skill.html'}, name='playguide_private_skill'),
    
    # アイテムの売買
    url(r'^playguide/buying/$', 'direct_to_template', {'template': 'playguide/buying.html'}, name='playguide_buying'),
    
    # トレード
    url(r'^playguide/trade_item/$', 'direct_to_template', {'template': 'playguide/trade_item.html'}, name='playguide_trade_item'),
    
    # バザー
    url(r'^playguide/bazzer/$', 'direct_to_template', {'template': 'playguide/bazzer.html'}, name='playguide_bazzer'),
    
    # フォーラムを利用する
    url(r'^playguide/bbs/$', 'direct_to_template', {'template': 'playguide/bbs.html'}, name='playguide_bbs'),
    
    # サイト内メッセージ
    url(r'^playguide/site_message/$', 'direct_to_template', {'template': 'playguide/site_message.html'}, name='playguide_site_message'),
    
    # リザルトメッセージ
    url(r'^playguide/message/$', 'direct_to_template', {'template': 'playguide/message.html'}, name='playguide_message'),
    
    # バトルセリフ
    url(r'^playguide/serif/$', 'direct_to_template', {'template': 'playguide/serif.html'}, name='playguide_serif'),
    
    # テキストコマンド
    url(r'^playguide/textcommand/$', 'direct_to_template', {'template': 'playguide/textcommand.html'}, name='playguide_textcommand'),
    
    # キャラクターの設定
    url(r'^playguide/chara_background/$', 'direct_to_template', {'template': 'playguide/chara_background.html'}, name='playguide_chara_background'),
    
    # アイコンの設定
    url(r'^playguide/chara_icon/$', 'direct_to_template', {'template': 'playguide/chara_icon.html'}, name='playguide_chara_icon'),
    
    # アカウントの管理
    url(r'^playguide/account/$', 'direct_to_template', {'template': 'playguide/account.html'}, name='playguide_account'),
    
    # クラス
    url(r'^playguide/installclass/$', 'direct_to_template', {'template': 'playguide/installclass.html'}, name='playguide_installclass'),
    
    # 装備
    url(r'^playguide/item_equipment/$', 'direct_to_template', {'template': 'playguide/item_equipment.html'}, name='playguide_item_equipment'),
    
    # 隊列
    url(r'^playguide/formation/$', 'direct_to_template', {'template': 'playguide/formation.html'}, name='playguide_formation'),
    
    # 戦術
    url(r'^playguide/customize/$', 'direct_to_template', {'template': 'playguide/customize.html'}, name='playguide_customize'),
    
    # バトルについて
    url(r'^playguide/battle/$', 'direct_to_template', {'template': 'playguide/battle.html'}, name='playguide_battle'),
    
    # ステータス変化
    url(r'^playguide/status/$', 'direct_to_template', {'template': 'playguide/status.html'}, name='playguide_status'),
    
    # クエストについて
    url(r'^playguide/event/$', 'direct_to_template', {'template': 'playguide/event.html'}, name='playguide_event'),
    
    # 能力値（アビリティ）
    url(r'^playguide/ability/$', 'direct_to_template', {'template': 'playguide/ability.html'}, name='playguide_ability'),
    
    # アイテムについて
    url(r'^playguide/item/$', 'direct_to_template', {'template': 'playguide/item.html'}, name='playguide_item'),
    
    # スキルについて
    url(r'^playguide/skill/$', 'direct_to_template', {'template': 'playguide/skill.html'}, name='playguide_skill'),
    
    # 冒険に役立つヒント
    url(r'^playguide/tips/$', 'direct_to_template', {'template': 'playguide/tips.html'}, name='playguide_tips'),
    
    # 改訂履歴
    url(r'^playguide/update/$', 'direct_to_template', {'template': 'playguide/update.html'}, name='playguide_update'),
    
    
    # result
    
    # リザルトインデックス
    url(r'^result/$', 'direct_to_template', {'template': 'result/index.html'}, name='result_index'),
    
    # ニュープレイヤー
    url(r'^result/newplayer.html$', 'direct_to_template', {'template': 'result/newplayer.html'}, name='result_newplayer'),
    
    # ダウンロードリンク
    url(r'^result/download/$', 'direct_to_template', {'template': 'result/download/index.html'}, name='result_download'),
    
    
    # worldguide
    
    # 世界背景
    url(r'^worldguide/$', 'direct_to_template', {'template': 'worldguide/index.html'}, name='worldguide_index'),
    
    # ファーネルド連邦
    url(r'^worldguide/farneld/$', 'direct_to_template', {'template': 'worldguide/farneld.html'}, name='worldguide_farneld'),
    
    # ワルド帝国
    url(r'^worldguide/wald/$', 'direct_to_template', {'template': 'worldguide/wald.html'}, name='worldguide_wald'),
    
    # ネルヴァリア王国
    url(r'^worldguide/nellvearia/$', 'direct_to_template', {'template': 'worldguide/nellvearia.html'}, name='worldguide_nellvearia'),
    
    # ダナクス諸侯連合
    url(r'^worldguide/danaks/$', 'direct_to_template', {'template': 'worldguide/danaks.html'}, name='worldguide_danaks'),
    
    # 公共機関
    url(r'^worldguide/office/$', 'direct_to_template', {'template': 'worldguide/office.html'}, name='worldguide_office'),
    
    # 輪郭
    url(r'^worldguide/outside/$', 'direct_to_template', {'template': 'worldguide/outside.html'}, name='worldguide_outside'),
    
    # 精霊と守護者
    url(r'^worldguide/elemental/$', 'direct_to_template', {'template': 'worldguide/elemental.html'}, name='worldguide_elemental'),
    
    # 神々
    url(r'^worldguide/gods/$', 'direct_to_template', {'template': 'worldguide/gods.html'}, name='worldguide_gods'),
    
    # 世界年表
    url(r'^worldguide/history/$', 'direct_to_template', {'template': 'worldguide/history.html'}, name='worldguide_history'),
    
    # 近代背景
    url(r'^worldguide/lastest/$', 'direct_to_template', {'template': 'worldguide/lastest.html'}, name='worldguide_lastest'),
    
    # 魔神戦争
    url(r'^worldguide/war/$', 'direct_to_template', {'template': 'worldguide/war.html'}, name='worldguide_war'),
    
    # クラス
    url(r'^worldguide/install/$', 'direct_to_template', {'template': 'worldguide/install.html'}, name='worldguide_install'),
    
    # 種族と相互関係
    url(r'^worldguide/race/$', 'direct_to_template', {'template': 'worldguide/race.html'}, name='worldguide_race'),
    
    
    
    
)

# アカウント
urlpatterns += patterns(
    'website.views.account',
    
    # ログイン
    url(r'^account/login/$', 'account_login', name='account_login'),
    
    # ログアウト
    url(r'^account/logout/$', 'account_logout', name='account_logout'),
    
    # 設定
    url(r'^account/setting/$', 'account_setting', name='account_setting'),
    
    # パスワードリセット
    url(r'^account/reset/$', 'account_password_reset', name='account_pass_reset'),
    
    # パスワード変更
    url(r'^account/prs/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'account_password_reset_changer', name='account_pass_reset_changer'),
    
    # メッセージリスト
    url(r'^message/$', 'message_list', name='account_message_list'),
    url(r'^message/(?P<page>\d+)/$', 'message_list', name='account_message_list'),
    
    # 送信済メッセージリスト
    url(r'^send_message/$', 'send_message_list', name='account_send_message_list'),
    url(r'^send_message/(?P<page>\d+)/$', 'send_message_list', name='account_send_message_list'),
    
    # メッセージ詳細
    url(r'^message/detail/(?P<message_id>\d+)/$', 'message_detail', name='account_message_detail'),
    
    # メッセージ作成
    url(r'^message/create/(?P<reply_message_id>\d+)/$', 'message_create', name='account_message_create'),
    
    # 設定
    url(r'^account/myresult/$', 'my_result', name='my_result'),
)

# フォーラム
urlpatterns += patterns(
    'website.views.forum',
    
    # フォーラムインデックス
    url(r'^forum/$', 'forum_index', name='forum_index'),
    
    # フォーラムリスト
    url(r'^forum/list/(?P<forum_id>\d+)/$', 'forum_list', name='forum_list'),
    url(r'^forum/list/(?P<forum_id>\d+)/(?P<page>\d+)/$', 'forum_list', name='forum_list'),
    
    # スレッド作成
    url(r'^forum/create/(?P<forum_id>\d+)/$', 'thread_create', name='forum_thread_create'),
    
    # スレッド作成(非認証)
    url(r'^forum/create/noauth/(?P<forum_id>\d+)/$', 'thread_create_notauth', name='forum_thread_create_notauth'),

    # スレッド詳細
    url(r'^forum/thread/(?P<forum_id>\d+)/(?P<thread_id>\d+)/$', 'thread_detail', name='forum_thread_detail'),
    url(r'^forum/thread/(?P<forum_id>\d+)/(?P<thread_id>\d+)/(?P<page>\d+)/$', 'thread_detail', name='forum_thread_detail'),
    
    # スレッド返信
    url(r'^forum/reply/(?P<forum_id>\d+)/(?P<thread_id>\d+)/$', 'thread_reply', name='forum_thread_reply'),
    url(r'^forum/reply/(?P<forum_id>\d+)/(?P<thread_id>\d+)/(?P<article_id>\d+)/$', 'thread_reply', name='forum_thread_reply'),
    
    # スレッド返信(非認証)
    url(r'^forum/reply/noauth/(?P<forum_id>\d+)/(?P<thread_id>\d+)/$', 'thread_reply_notauth', name='forum_thread_reply_notauth'),
    url(r'^forum/reply/noauth/(?P<forum_id>\d+)/(?P<thread_id>\d+)/(?P<article_id>\d+)/$', 'thread_reply_notauth', name='forum_thread_reply_notauth'),

    # 記事編集
    url(r'^forum/edit/(?P<forum_id>\d+)/(?P<thread_id>\d+)/(?P<article_id>\d+)/$', 'article_edit', name='forum_article_edit'),

    # 記事削除
    url(r'^forum/delete/(?P<forum_id>\d+)/(?P<thread_id>\d+)/(?P<article_id>\d+)/$', 'article_delete', name='forum_article_delete'),

    # 記事検索
    url(r'^forum/search/$', 'search', name='forum_search'),

    # Ajaxいいね
    url(r'^forum/good/(?P<article_id>\d+)/$', 'so_good', name='forum_good'),
    
)

# 登録
urlpatterns += patterns(
    'website.views.regist',

    # 登録インデックス
    url(r'^continue/$', 'index', name='regist_index'),

)

# 新規登録
urlpatterns += patterns(
    'website.views.register.newgame',

    # 登録インデックス
    url(r'^new_game/$', 'index', name='newgame_index'),
    
    # 登録完了
    url(r'^new_game/complete/$', 'complete', name='newgame_complete'),
    
    # 登録コンペア
    url(r'^new_game/compr/(?P<activate_hash>.+)/$', 'compare', name='newgame_compare'),

)

# 継続登録
urlpatterns += patterns(
    'website.views.register.continue_main',

    # 登録インデックス
    url(r'^continue/main/$', 'index', name='continue_main_index'),
    
    # 登録確認
    url(r'^continue/main/confirm/$', 'confirm', name='continue_main_confirm'),
    
    # 登録実行
    url(r'^continue/main/execute/$', 'execute', name='continue_main_execute'),
    
    # 登録完了
    url(r'^continue/main/complete/$', 'complete', name='continue_main_complete'),

    # Ajaxマークロード
    url(r'^continue/load_mark/(?P<quest_id>\d+)/$', 'select_mark', name='continue_select_mark'),

)

# 戦闘準備登録
urlpatterns += patterns(
    'website.views.register.continue_equip',

    # 登録インデックス
    url(r'^continue/equip/$', 'index', name='continue_equip_index'),
    
    # 登録確認
    url(r'^continue/equip/confirm/$', 'confirm', name='continue_equip_confirm'),
    
    # 登録実行
    url(r'^continue/equip/execute/$', 'execute', name='continue_equip_execute'),
    
    # 登録完了
    url(r'^continue/equip/complete/$', 'complete', name='continue_equip_complete'),

)

# 取引登録
urlpatterns += patterns(
    'website.views.register.continue_trade',

    # 登録インデックス
    url(r'^continue/trade/$', 'index', name='continue_trade_index'),
    
    # 登録確認
    url(r'^continue/trade/confirm/$', 'confirm', name='continue_trade_confirm'),
    
    # 登録実行
    url(r'^continue/trade/execute/$', 'execute', name='continue_trade_execute'),
    
    # 登録完了
    url(r'^continue/trade/complete/$', 'complete', name='continue_trade_complete'),

    # Ajaxマークロード
    url(r'^continue/load_shop/(?P<category_id>\d+)/$', 'item_data', name='continue_item_data'),

)

# 戦術登録
urlpatterns += patterns(
    'website.views.register.continue_battleaction',

    # 登録インデックス
    url(r'^continue/action/$', 'index', name='continue_battleaction_index'),
    
    # 登録確認
    url(r'^continue/action/confirm/$', 'confirm', name='continue_battleaction_confirm'),
    
    # 登録実行
    url(r'^continue/action/execute/$', 'execute', name='continue_battleaction_execute'),
    
    # 登録完了
    url(r'^continue/action/complete/$', 'complete', name='continue_battleaction_complete'),

)

# 個人設定
urlpatterns += patterns(
    'website.views.register.continue_profile',

    # 登録インデックス
    url(r'^continue/profile/$', 'index', name='continue_profile_index'),
    
    # 登録確認
    url(r'^continue/profile/confirm/$', 'confirm', name='continue_profile_confirm'),
    
    # 登録実行
    url(r'^continue/profile/execute/$', 'execute', name='continue_profile_execute'),
    
    # 登録完了
    url(r'^continue/profile/complete/$', 'complete', name='continue_profile_complete'),

)

# アイコン設定
urlpatterns += patterns(
    'website.views.register.continue_icon',

    # 登録インデックス
    url(r'^continue/icon/$', 'index', name='continue_icon_index'),
    
    # 登録確認
    url(r'^continue/icon/confirm/$', 'confirm', name='continue_icon_confirm'),
    
    # 登録実行
    url(r'^continue/icon/execute/$', 'execute', name='continue_icon_execute'),
    
    # 登録完了
    url(r'^continue/icon/complete/$', 'complete', name='continue_icon_complete'),

)

# メッセージ登録
urlpatterns += patterns(
    'website.views.register.continue_message',

    # 登録インデックス
    url(r'^continue/message/$', 'index', name='continue_message_index'),
    
    # 登録確認
    url(r'^continue/message/confirm/$', 'confirm', name='continue_message_confirm'),
    
    # 登録実行
    url(r'^continue/message/execute/$', 'execute', name='continue_message_execute'),
    
    # 登録完了
    url(r'^continue/message/complete/$', 'complete', name='continue_message_complete'),

)

# セリフ設定
urlpatterns += patterns(
    'website.views.register.continue_serif',

    # 登録インデックス
    url(r'^continue/serif/$', 'index', name='continue_serif_index'),
    
    # 登録確認
    url(r'^continue/serif/confirm/$', 'confirm', name='continue_serif_confirm'),
    
    # 登録実行
    url(r'^continue/serif/execute/$', 'execute', name='continue_serif_execute'),
    
    # 登録完了
    url(r'^continue/serif/complete/$', 'complete', name='continue_serif_complete'),

)

# 登録内容確認
urlpatterns += patterns(
    'website.views.register.confirm',

    # 登録インデックス
    url(r'^continue/confirm/$', 'index', name='continue_confirm_index'),
    
    # 登録完了
    url(r'^continue/confirm/complete/$', 'complete', name='continue_confirm_complete'),

)

# 冒険の結果
urlpatterns += patterns(
    'website.views.result',

    # キャラクター検索
    url(r'^result/search/$', 'search', name='result_search'),
    
    # リスト
    url(r'^result/list(?P<page>\d{4}).html$', 'chara_list', name='result_chara_list'),
    
    # リスト(リストメッセージ)
    url(r'^result/lcom(?P<page>\d{4}).html$', 'chara_com_list', name='result_chara_message_list'),
    
    # プライベート結果
    url(r'^result/status/character(?P<entry>\d{4}).html$', 'private_status', name='result_private_status'),
    
    # パーティ結果
    url(r'^result/party/party(?P<party>\d{4}).html$', 'party_status', name='result_party_status'),
    
)

# リンク
urlpatterns += patterns(
    'website.views.link',

    # リンクインデックス
    url(r'^link/$', 'link_index', name='link_index'),
    
    # リンク申請・変更
    url(r'^link/regist/$', 'register', name='link_register'),

)

# バザー
urlpatterns += patterns(
    'website.views.bazzer',

    # バザーインデックス
    url(r'^bazzer/$', 'bazzer_list', name='bazzer_list'),
    
    # バザー詳細
    url(r'^bazzer/detail/(?P<bazzer_id>\d+)/$', 'detail', name='bazzer_detail'),
    
    # バザー出品
    url(r'^bazzer/sell/$', 'sell_register', name='bazzer_sell_register'),
    
    # バザー出品完了
    url(r'^bazzer/sell/complete/(?P<bazzer_id>\d+)/$', 'sell_complete', name='bazzer_sell_complete'),
    
    # バザー購入
    url(r'^bazzer/buy/(?P<bazzer_id>\d+)/$', 'buy', name='bazzer_buy'),
    
    # バザー購入完了
    url(r'^bazzer/complete/buy/(?P<bazzer_id>\d+)/$', 'buy_complete', name='bazzer_buy_complete'),
    
    # バザーキャンセル
    url(r'^bazzer/cancel/(?P<bazzer_id>\d+)/$', 'cancel', name='bazzer_cancel'),
    
    # バザーキャンセル完了
    url(r'^bazzer/complete/cancel/(?P<bazzer_id>\d+)/$', 'cancel_complete', name='bazzer_cancel_complete'),

)

# データ
urlpatterns += patterns(
    'website.views.data',

    # クラスデータ
    url(r'^playguide/installclass/detail/(?P<install_id>\d+)/$', 'install_data', name='install_data'),
    
    # ウェポンデータ
    url(r'^playguide/item_equipment/detail/(?P<weapon_id>\d+)/$', 'weapon_data', name='weapon_data'),
    
    # プライベートスキル
    url(r'^playguide/private_skill/detail/$', 'private_data', name='private_data'),
    
    # 防具データ
    url(r'^playguide/item_equipment/detail/protect/(?P<protect_id>\d+)/$', 'protect_data', name='protect_data'),
    
    # 販売データ
    url(r'^playguide/sell_item/(?P<category_id>\d+)/$', 'sell_data', name='sell_data'),
    url(r'^playguide/sell_item/$', 'sell_data', name='sell_data'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^500/$', 'website.views.root.server_error'),
    )
