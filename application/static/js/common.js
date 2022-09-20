
//##################################################################################################
//extend
Function.prototype.bind = function (thisobj) {
	var f = this;
	return function(){
		return f.apply(thisobj,arguments);
	};
};
$.fn.check = function (val) {
	if (typeof val == 'undefined') {
		return !!this.attr('checked');
	} else {
		var chk = this[0].getAttribute('checked');
		if (val == 'not') {
			// 文字列で'not'ならひっくり返す
			if (chk) {
				this[0].removeAttribute('checked');
			} else {
				this[0].setAttribute('checked','checked');
			}
		} else if (val) {
			this.attr('checked','checked');
		} else {
			this.removeAttr('checked');
		}
		return this;
	}
};
$.fn.disableOnSubmit = function(disableList){
	
	if(disableList == null){var $list = 'input[type=submit],input[type=button],input[type=reset],button';}
	else{var $list = disableList;}
	
	// Makes sure button is enabled at start
	$(this).find($list).removeAttr('disabled');
	
	$(this).submit(function(){$(this).find($list).attr('disabled','disabled');});
	return this;
};

//##################################################################################################
//browser
var browser = {
	ie : '\v'=='v',
	moz : ('mozInnerScreenX' in window),
	webkit : ('webkitConvertPointFromNodeToPage' in window),
	pc : !('ontouchstart' in document),
	local : /^(192\.168\.|127\.0\.0\.1|10\.0\.2\.)/.test(document.domain)
};

browser.pc = browser.pc || browser.moz || browser.ie;
browser.ios = (
	browser.webkit &&
	/iPhone|iPad|iPod/.test(navigator.platform) &&
	('ongesturestart' in document)
);
browser.android = (
	browser.webkit &&
	/Linux/.test(navigator.platform) &&
	!browser.pc &&
	!browser.ios
);

if (browser.android) {
	browser.ver = /Android ([\d\.]+)/.test(navigator.userAgent) ? parseFloat(RegExp.$1) : 0 ;
} else if (browser.ios) {
	browser.ver = /iPhone OS ([\d_]+)/.test(navigator.userAgent) ? parseFloat(RegExp.$1.replace(/_/,'.')) : 0 ;
}

var GrandBlaze = function () {
	
	var self = this;
	$(function(){
		GrandBlaze.prototype.onReady.apply(self);
	});
	$(window).bind('load',function(){
		GrandBlaze.prototype.onLoad.apply(self);
	});
	this.init();
	
	return this;
};

GrandBlaze.prototype = { //instance methods
	//
	//初期化処理。domロード前
	init : function () {
		
		this.zoom = 1;
		
		if (browser.ios) {//ios
			document.write('<style>header{ -webkit-transform:translateZ(0);} footer{ -webkit-transform:translateZ(0);} .container{-webkit-transform:translateZ(0);}</style>');
		} else if (browser.android && browser.ver >= 2.2) {//android
			if (window.innerWidth != 320) {
				var z = (window.innerWidth-1) / 320;
				document.write('<style>:root{zoom:'+z+';}</style>');
				this.zoom = z;
			}
			
		}
	},
	//domのロード後
	onReady : function () {
		var self = this;
		
		showhelp = '';
		
		showitem = -1;
		
		$('section.dialog-base').dialog({
		    bgiframe: true,
		    autoOpen: false,
		    width: browser.pc ? 680 : 320,
		    modal: true,
		    height: browser.pc ? 600 : 320,
		    buttons: {
		        '閉じる': function(){
		            $(this).dialog('close');
		        }
		    }
		});
		
		$('input[type="button"].dialog-open').click(function(){
			var target_dialog = $(this).data('dialog');
		    var return_id = $(this).data('return_id');
		    var return_value = $(this).data('return_value');
            var return_count = $(this).data('return_count');
            var return_money = $(this).data('return_money');
            var title_name = $(this).data('title');
            var target_dialog_input = $('#dialog-' + target_dialog);
		    target_dialog_input.find('input[type="hidden"].ret_id').val(return_id);
		    target_dialog_input.find('input[type="hidden"].ret_value').val(return_value);
		    if(return_count != null){
		    	target_dialog_input.find('input[type="hidden"].ret_count').val(return_count);
		    }
            if(return_money != null){
            	target_dialog_input.find('input[type="hidden"].ret_money').val(return_money);
            }
            if(title_name != null){
                target_dialog_input.dialog('option', 'title', title_name);
            }
			target_dialog_input.dialog('open');
		});
		
		$('a.apply-link').click(this.applyLink);
		
		$('form').disableOnSubmit();
		
		$('#itemdata a').each(function(i){
			$(this).click(function(){
				var view_target = $(this).data('viewer');
				var itemdata = $('#itemdata');
				var itemdata_tbody = itemdata.find('tbody');
				if (view_target == 'all'){
					itemdata_tbody.find('tr').show();
				}
				else{
					itemdata_tbody.find('tr.' + view_target).show();
					itemdata_tbody.find('tr:not(.' + view_target + ')').hide();
				}
				var itemdata_li = itemdata.find('li');
				itemdata_li.attr('class', 'ui-state-default ui-corner-top');
				itemdata_li.eq(i).attr('class', 'ui-state-default ui-corner-top ui-tabs-selected ui-state-active');
			});
		});
		
		$('#prvdata a').each(function(i){
			$(this).click(function(){
				var view_target = $(this).data('viewer');
				var prvdata = $('#prvdata');
				var prvdata_tbody = prvdata.find('tbody');
				if (view_target == 'all'){
					prvdata_tbody.find('tr').show();
				}
				else{
					prvdata_tbody.find('tr.' + view_target).show();
					prvdata_tbody.find('tr:not(.' + view_target + ')').hide();
				}
				var prvdata_li = prvdata.find('li');
				prvdata_li.attr('class', 'ui-state-default ui-corner-top');
				prvdata_li.eq(i).attr('class', 'ui-state-default ui-corner-top ui-tabs-selected ui-state-active');
			});
		});
		
		$('#keydata a').each(function(i){
			$(this).click(function(){
				var view_target = $(this).data('viewer');
				var keydata = $('#keydata');
				var keydata_tbody = keydata.find('tbody');
				if (view_target == 'all'){
					keydata_tbody.find('tr').show();
				}
				else{
					keydata_tbody.find('tr.' + view_target).show();
					keydata_tbody.find('tr:not(.' + view_target + ')').hide();
				}
				var keydata_li = keydata.find('li');
				keydata_li.attr('class', 'ui-state-default ui-corner-top');
				keydata_li.eq(i).attr('class', 'ui-state-default ui-corner-top ui-tabs-selected ui-state-active');
			});
		});
		
		$('#compque').button({
            text: true
		}).click(function(){
			$('#compquelist').toggle('fast');
		});
		
		$('table.list_data').find('tbody').find('tr').click(function(){
			var idx = $(this).index();
			$('table.list_data').find('tbody').find('tr').find('div.toolhelp').hide();
			var toolhelp = $(this).find('div.toolhelp');
			toolhelp.toggle();
			if(idx == showitem) {
				showitem = -1;
				toolhelp.hide();
			}
			else {
				showitem = idx;				
			}
		});
		
		var form_widget = $('div.form-widget');
		
		form_widget.click(function(){
			$('div.help').hide();
		});
		form_widget.find('a.help').click(function(e){
			$('div.help').hide();
			var target = $(this).data('help');
			var help_target = $('#help-' + target); 
			help_target.toggle();
			if(target == showhelp) {
				showhelp = '';
				help_target.hide();
			}
			else {
				showhelp = target;				
			}
			
			grb.stopPropagation(e || window.event);
		});
		
		$('#id_quest_id').change(this.markAjax);
		
		$('#btactlist').find('div.form-widget').formset({
	        addText: '行の追加',
	        deleteText: '行削除',
	        addCssClass: 'addbtlist',
	        deleteCssClass: 'deletebtlist',
	        maxList: 10,
	        added: function(row){
	        	$("a.deletebtlist").button({
		            icons: {
		                primary: "ui-icon-circle-minus"
		            },
		            text: true
				});
				var length = parseInt($('#id_form-TOTAL_FORMS').val());
				var btlist = $('#btactlist').children('div');
				var count = 0;
				for(var i=0;i<length;i++){
					var btlist_eq = btlist.eq(i);
					btlist_eq.find('span.action_no').text(count+1);
					var btlist_eq_eq0 = btlist_eq.children('div').eq(0);
					var btlist_eq_eq1 = btlist_eq.children('div').eq(1);
					btlist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-action_target');
					btlist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-action_target');
					btlist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-action');
					btlist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-action');
                    var btlist_eq_delete = btlist_eq.find('input:hidden[id $= "-DELETE"]');
                    if(!btlist_eq_delete.length || btlist_eq_delete.val() != 'on'){
                        count++;
                    }
				}
				$('input:button.dialog-open').val('選択');
				if (length >= 9){
					$('a.addbtlist').hide();
				}
				
				$(row).find('div.value').find('span').text('');
				
                $('#btactlist').sortable({
                    cursor: 'move',
                    opacity: 0.7,
                    axis: 'y',
                    placeholder: 'ui-state-highlight',
                    forcePlaceholderSize: true,
                    update: function(){
                        var forms = $('.dynamic-form').not('.formset-custom-template');
                        $('#id_form-TOTAL_FORMS').val(forms.length);
                        var btlist = $('#btactlist').children('div');
                        var count = 0;
                        for (var i=0, formCount=forms.length; i<formCount; i++) {
                        	var btlist_eq = btlist.eq(i);
                            btlist_eq.find('span.action_no').text(count+1);
							var btlist_eq_eq0 = btlist_eq.children('div').eq(0);
							var btlist_eq_eq1 = btlist_eq.children('div').eq(1);
                            btlist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-action_target');
                            btlist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-action_target');
                            btlist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-action');
                            btlist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-action');
                            btlist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-action');
                            var btlist_eq_delete = btlist_eq.find('input:hidden[id $= "-DELETE"]');
                            if(!btlist_eq_delete.length || btlist_eq_delete.val() != 'on'){
                                count++;
                            }
                            forms.eq(i).find('input,select,textarea,label,span').each(function() {
                                grb.updateElementIndex($(this), 'form', i);
                            });
                        }
                    }
                });
	        },
	        removed: function(){
				var length = parseInt($('#id_form-TOTAL_FORMS').val());
				var btlist = $('#btactlist').children('div');
				for(var i=0;i<length;i++){
					var btlist_eq = btlist.eq(i);
					btlist_eq.find('span.action_no').text(i+1);
					var btlist_eq_eq0 = btlist_eq.children('div').eq(0);
					var btlist_eq_eq1 = btlist_eq.children('div').eq(1);
					btlist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-action_target');
					btlist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-action_target');
					btlist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-action');
					btlist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-action');
					$('a.addbtlist').show();
				}
	        }
        });
        $('#btactlist').sortable({
            cursor: 'move',
            opacity: 0.7,
            axis: 'y',
            placeholder: 'ui-state-highlight',
            forcePlaceholderSize: true,
            update: function(){
                var forms = $('.dynamic-form').not('.formset-custom-template');
                $('#id_form-TOTAL_FORMS').val(forms.length);
                var btlist = $('#btactlist').children('div');
                for (var i=0, formCount=forms.length; i<formCount; i++) {
                    forms.eq(i).find('input,select,textarea,label,span').each(function() {
                    	var btlist_eq = btlist.eq(i);
                        btlist_eq.find('span.action_no').text(i+1);
						var btlist_eq_eq0 = btlist_eq.children('div').eq(0);
						var btlist_eq_eq1 = btlist_eq.children('div').eq(1);
                        btlist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-action_target');
                        btlist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-action_target');
                        btlist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-action');
                        btlist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-action');
                        forms.eq(i).find('input,select,textarea,label,span').each(function() {
                            grb.updateElementIndex($(this), 'form', i);
                        });
                    });
                }
            }
        });
		
		$('#iclist').find('div.form-widget').formset({
	        addText: '行の追加',
	        deleteText: '行削除',
	        addCssClass: 'addbtlist',
	        deleteCssClass: 'deletebtlist',
	        added: function(row){
	        	$("a.deletebtlist").button({
		            icons: {
		                primary: "ui-icon-circle-minus"
		            },
		            text: true
				});
				var length = parseInt($('#id_form-TOTAL_FORMS').val());
                var iclist = $('#iclist').children('div');
				for(var i=0;i<length;i++){
					var iclist_eq = iclist.eq(i);
					iclist_eq.find('span.icon_no').text(i+1);
					var iclist_eq_eq0 = iclist_eq.children('div').eq(0);
					var iclist_eq_eq1 = iclist_eq.children('div').eq(1);
					iclist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-icon_url');
					iclist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-icon_url');
					iclist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-icon_copyright');
					iclist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-icon_copyright');
				}
				if (length >= 49){
					$('a.addbtlist').hide();					
				}
	        },
	        removed: function(){
				var length = parseInt($('#id_form-TOTAL_FORMS').val());
                var iclist = $('#iclist').children('div');
				for(var i=0;i<length;i++){
					var iclist_eq = iclist.eq(i);
					iclist_eq.find('span.icon_no').text(i+1);
					var iclist_eq_eq0 = iclist_eq.children('div').eq(0);
					var iclist_eq_eq1 = iclist_eq.children('div').eq(1);
					iclist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-icon_url');
					iclist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-icon_url');
					iclist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-icon_copyright');
					iclist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-icon_copyright');
					$('a.addbtlist').show();
				}
	        }
        });
		
		$('#mslist').find('div.form-widget').formset({
	        addText: '行の追加',
	        deleteText: '行削除',
	        addCssClass: 'addbtlist',
	        deleteCssClass: 'deletebtlist',
	        added: function(row){
	        	row.find('select').val('0');
	        	row.find('text').val('');
	        	row.find('textarea').val('');
	        	$("a.deletebtlist").button({
		            icons: {
		                primary: "ui-icon-circle-minus"
		            },
		            text: true
				});
				var length = parseInt($('#id_form-TOTAL_FORMS').val());
                var mslist = $('#mslist').children('div');
				for(var i=0;i<length;i++){
					var mslist_eq = mslist.eq(i);
					mslist_eq.find('span.mes_no').text(i+1);
					var mslist_eq_eq0 = mslist_eq.children('div').eq(0);
					var mslist_eq_eq1 = mslist_eq.children('div').eq(1);
					var mslist_eq_eq2 = mslist_eq.children('div').eq(2);
					mslist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-message_target');
					mslist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-message_target');
					mslist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-message_entry');
					mslist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-message_entry');
					mslist_eq_eq2.find('a.help').attr('data-help', parseInt(i) + '-message_body');
					mslist_eq_eq2.find('div.help').attr('id', 'help-' + parseInt(i) + '-message_body');
				}
	        },
	        removed: function(){
				var length = parseInt($('#id_form-TOTAL_FORMS').val());
                var mslist = $('#mslist').children('div');
				for(var i=0;i<length;i++){
					var mslist_eq = mslist.eq(i);
					mslist_eq.find('span.mes_no').text(i+1);
					var mslist_eq_eq0 = mslist_eq.children('div').eq(0);
					var mslist_eq_eq1 = mslist_eq.children('div').eq(1);
					var mslist_eq_eq2 = mslist_eq.children('div').eq(2);
					mslist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-message_target');
					mslist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-message_target');
					mslist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-message_entry');
					mslist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-message_entry');
					mslist_eq_eq2.find('a.help').attr('data-help', parseInt(i) + '-message_body');
					mslist_eq_eq2.find('div.help').attr('id', 'help-' + parseInt(i) + '-message_body');
					$('a.addbtlist').show();
				}
	        }
        });
		
		$('#sflist').find('div.form-widget').formset({
	        addText: '行の追加',
	        deleteText: '行削除',
	        addCssClass: 'addbtlist',
	        deleteCssClass: 'deletebtlist',
	        added: function(row){
	        	$("a.deletebtlist").button({
		            icons: {
		                primary: "ui-icon-circle-minus"
		            },
		            text: true
				});
				var length = parseInt($('#id_form-TOTAL_FORMS').val());
                var sflist = $('#sflist').children('div');
				for(var i=0;i<length;i++){
					var sflist_eq = sflist.eq(i);
					sflist_eq.find('span.word_no').text(i+1);
					var sflist_eq_eq0 = sflist_eq.children('div').eq(0);
					var sflist_eq_eq1 = sflist_eq.children('div').eq(1);
					var sflist_eq_eq2 = sflist_eq.children('div').eq(2);
					sflist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-situation_id');
					sflist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-situation_id');
					sflist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-perks_id');
					sflist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-perks_id');
					sflist_eq_eq2.find('a.help').attr('data-help', parseInt(i) + '-serif_text');
					sflist_eq_eq2.find('div.help').attr('id', 'help-' + parseInt(i) + '-serif_text');
				}
				$('input:button.dialog-open').val('選択');
				$(row).find('div.value span').text('');
				$(row).find('textarea').val('');
	        },
	        removed: function(){
				var length = parseInt($('#id_form-TOTAL_FORMS').val());
                var sflist = $('#sflist').children('div');
				for(var i=0;i<length;i++){
					var sflist_eq = sflist.eq(i);
					sflist_eq.find('span.word_no').text(i+1);
					var sflist_eq_eq0 = sflist_eq.children('div').eq(0);
					var sflist_eq_eq1 = sflist_eq.children('div').eq(1);
					var sflist_eq_eq2 = sflist_eq.children('div').eq(2);
					sflist_eq_eq0.find('a.help').attr('data-help', parseInt(i) + '-situation_id');
					sflist_eq_eq0.find('div.help').attr('id', 'help-' + parseInt(i) + '-situation_id');
					sflist_eq_eq1.find('a.help').attr('data-help', parseInt(i) + '-perks_id');
					sflist_eq_eq1.find('div.help').attr('id', 'help-' + parseInt(i) + '-perks_id');
					sflist_eq_eq2.find('a.help').attr('data-help', parseInt(i) + '-serif_text');
					sflist_eq_eq2.find('div.help').attr('id', 'help-' + parseInt(i) + '-serif_text');
					$('a.addbtlist').show();
				}
	        }
        });
		
		$("a.addbtlist").button({
            icons: {
                primary: "ui-icon-circle-plus"
            },
            text: true
		});
		
		$("a.deletebtlist").button({
            icons: {
                primary: "ui-icon-circle-minus"
            },
            text: true
		});
		
		$('#targetdata li a').each(function(i){
			$(this).click(function(){
				var view_target = $(this).data('viewer');
				var targetdata = $('#targetdata');
				var targetdata_tbody = targetdata.find('tbody');
				targetdata_tbody.find('tr.' + view_target).show();
				targetdata_tbody.find('tr:not(.' + view_target + ')').hide();
				var targetdata_li = targetdata.find('li');
				targetdata_li.attr('class', 'ui-state-default ui-corner-top');
				targetdata_li.eq(i).attr('class', 'ui-state-default ui-corner-top ui-tabs-selected ui-state-active');
			});
		});
		
		$('#shopitemdata>ul>li>a').each(function(i){
			$(this).click(function(){
				var view_target = $(this).data('viewer');
				$('#view-type1').hide();
				$('#view-type2').hide();
				$('#view-type3').hide();
				$('#view-type4').hide();
				$('#view-type5').hide();
				$('#view-type6').hide();
				$('#view-' + view_target).show();
				var shopdata = $('#shopitemdata>ul>li');
				shopdata.attr('class', 'ui-state-default ui-corner-top');
				shopdata.eq(i).attr('class', 'ui-state-default ui-corner-top ui-tabs-selected ui-state-active');
			});
		});
		
		$('#shopitemdata div li a').each(function(i){
			$(this).click(function(){
				var view_target = $(this).data('viewer');
				$('#id_shopcategory').val(view_target);
				grb.shopAjax();
				var shodata = $('#shopitemdata').find('div').find('li');
				shodata.attr('class', 'ui-state-default ui-corner-top');
				shodata.eq(i).attr('class', 'ui-state-default ui-corner-top ui-tabs-selected ui-state-active');
			});
		});
		
        for(i=0; i<5; i++){
            $('input[name="money-' + i + '-trade_number"]').change(this.calcMoney);
        }
        
        if(!browser.pc){
            $('#sidebar1').find('nav').accordion({
                header: 'h4',
                heightStyle: 'content',
                autoHeight: false,
                icons: false,
                collapsible: true,
                active: false
            });
        }
		
		// Androidでselectタグの表示が更新されないことがあるバグ対策
		if(browser.android) {
			$('select').change(function(){
				this.style.display = 'none';
				var self = this;
				setTimeout(function(){
					self.style.display = 'inline-block';
				},0);
			});
		}
		
		if (this.onReady !== arguments.callee) {
			this.onReady.apply(this);
		}
		
	},
	//画像を含め読み込み終了時に呼ばれる
	onLoad : function () {
		
	},
	mark : {
		_response : function (data) {
			
			$('#id_mark_id').empty();
			var mark_select = document.getElementById("id_mark_id");
			var count = 0;
			
            $('#weabody').empty();
            var number = 1;
			
			for (key in data.marklist){
				mark_select.options[count] = new Option(data.marklist[key][1], data.marklist[key][0]);
				// 天候のリストを出す！
				
				if(data.weathers[0].length > 0){
				    $('#weather_button').data('title', $('#id_quest_id option:selected').text() + 'の天気予報');
				    $('#weather_button').show();
                    $('#weabody').append(
                        $('<tr>').append(
                            $('<td>').text(data.marklist[key][1])
                        ).append(
                            $('<td>').html('次の天気は <strong>' + data.weathers[count][0] + '</strong> になるでしょう。<br />翌週は <strong>' + data.weathers[count][1] + '</strong> に。<br />翌々週は <strong>' + data.weathers[count][2] + '</strong> になる見込みです。')
                        )
                    );
                }
                else{
                    $('#weather_button').hide();
                }
				
				count++;
			}
			
		}
	},
	shop : {
		_response : function (data) {
			
			$('#shopbody').empty();
			var number = 1;
			for (key in data.itemlist){
				$('#shopbody').append(
					$('<tr>').append(
						$('<td>').attr('rowspan', '2').text(data.itemlist[key].id)
					).append(
						$('<td>').append(
							$('<a>').attr('href','javascript:void(0)').addClass('apply-link').attr('data-dialog','shop_item').attr('data-id_value', data.itemlist[key].id).attr('data-name_value',data.itemlist[key].name).text(data.itemlist[key].name).click(grb.applyLink)
						)
					).append(
						$('<td>').text(data.itemlist[key].it_price)
					)
				).append(
					$('<tr>').append(
						$('<td>').attr('colspan', '2').html(data.itemlist[key].it_comment)
					)
				);
				number += 1;
			}
			
		}
	},
	good : {
		_response : function (data) {
			
			$('#id_good_count_' + data.article_id).html(data.goodcount);
			
		}
	},
    markAjax:function(){
    	quest_id = $('#id_quest_id').val();

		grb.response = false;
		$.ajax({
			async : true,
			url : '/continue/load_mark/' + quest_id + '/?'+(new Date()).getTime(),
			cache : true, //勝手にパラメータつくのを防止
			dataType : 'json',
			error : function(XMLHttpRequest, textStatus, errorThrown){
				if(!browser.local) location.reload();
			},
			success : grb.mark._response,
			timeout : 20000
		});
	},
    shopAjax:function(){
    	category_id = $('#id_shopcategory').val();

		grb.response = false;
		$.ajax({
			async : true,
			url : '/continue/load_shop/' + category_id + '/?'+(new Date()).getTime(),
			cache : true, //勝手にパラメータつくのを防止
			dataType : 'json',
			error : function(XMLHttpRequest, textStatus, errorThrown){
				if(!browser.local) location.reload();
			},
			success : grb.shop._response,
			timeout : 20000
		});
	},
    goodAjax:function(articleid){
    	article_id = articleid;

		grb.response = false;
		$.ajax({
			async : true,
			url : '/forum/good/' + article_id + '/?'+(new Date()).getTime(),
			cache : true, //勝手にパラメータつくのを防止
			dataType : 'json',
			error : function(XMLHttpRequest, textStatus, errorThrown){
				if(!browser.local) location.reload();
			},
			success : grb.good._response,
			timeout : 20000
		});
	},
    applyLink:function(){
	    var target_dialog = $(this).data('dialog');
	    var target_id = $('#dialog-' + target_dialog + ' input[type="hidden"].ret_id').val();
	    var target_name = $('#dialog-' + target_dialog + ' input[type="hidden"].ret_value').val();
        var target_count = $('#dialog-' + target_dialog + ' input[type="hidden"].ret_count').val();
        var target_money = $('#dialog-' + target_dialog + ' input[type="hidden"].ret_money').val();
	    
	    var value_id = $(this).data('id_value');
        var value_name = $(this).data('name_value');
        var value_count = $(this).data('count_value');
        var value_money = $(this).data('money_value');
        
        $('#' + target_id).val(value_id);
        $('#' + target_name).text(value_name);
        $('#' + target_count).text(value_count);
        $('#' + target_money).text(value_money);
        $('#dialog-' + target_dialog).dialog('close');
        
        grb.calcMoney();
	},
	calcMoney:function(){
	    var money = parseInt($('#hide_havemoney').val());
	    
	    $('input[name="add_money"]').each(function(i){
	        add = parseInt($(this).val());
	        if(!isNaN(add)){
	            money += add;
	        }
	    });
	    
        $('input[name="minus_money"]').each(function(i){
            minus = parseInt($(this).val());
            if(!isNaN(minus)){
                money -= minus;
            }
        });
        
        for(i=0; i<5; i++){
            tmp_money = parseInt($('input[name="money-' + i + '-trade_number"]').val());
            if(!isNaN(tmp_money)){
                money -= tmp_money;
            }
        }
        
        if(money < 0){
            money = money.toString().replace(/(\d)(?=(\d\d\d)+$)/g, '$1,');
            $('#id_havemoney').text(money).css('color', '#f30');
        }
        else{
            money = money.toString().replace(/(\d)(?=(\d\d\d)+$)/g , '$1,');
            $('#id_havemoney').text(money).css('color', '#D0D0D0');
        }
	},
    updateElementIndex:function(elem, prefix, ndx) {
        var idRegex = new RegExp('(' + prefix + '-\\d+-)|(^)'),
            replacement = prefix + '-' + ndx + '-';
        if (elem.attr("for")) elem.attr("for", elem.attr("for").replace(idRegex, replacement));
        if (elem.attr('id')) elem.attr('id', elem.attr('id').replace(idRegex, replacement));
        if (elem.attr('name')) elem.attr('name', elem.attr('name').replace(idRegex, replacement));
        if (elem.attr('data-return_id')) elem.attr('data-return_id', elem.attr('data-return_id').replace(idRegex, replacement));
        if (elem.attr('data-return_value')) elem.attr('data-return_value', elem.attr('data-return_value').replace(idRegex, replacement));
    },
    stopPropagation:function(ev){
    	if(ev.stopPropagation){
			ev.stopPropagation();
		}else{
			ev.cancelBubble = true;
		}
    },
    hiddenImage:function(target_id){
    	$('#'+target_id).val('http://www.grand-blaze.com/default.gif');
    },
    defaultImage:function(target_id){
    	$('#'+target_id).val('http://www.grand-blaze.com/defimage.gif');
    }
    
	
};


var grb = new GrandBlaze();