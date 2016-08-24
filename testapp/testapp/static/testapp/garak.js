// variables

width = $(window).width();
height = $(window).height();

// global function

function current_tab(href) { // 탭 이동할 때 마다 실행되는 스크립트
	var tab_id = href.slice('-1');

	switch (tab_id) {
		case '1':
			board.show();
			break;
		case '2':
			board.show();
			break;
		case '3':
			board.hide();
			break;
		default:
			console.log('default');
	}
}

function load(target, url) {  // target = HTML DOM, url에서 로딩된걸 집어넣음
	$.ajax({
		url: url,
		cache: false,
		method: "GET"
	})
		.done(function(data) {
			// alert("Data Loaded : " + msg);
			$(target).html(data);

		})
		.fail(function() {
			alert("failed");
		});
}

function commas_checker(x) {
	console.log('요거 만들어야 할듯');
}

function commas(x) {
	return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function de_commas(x) {
	return x.toString().split(',').join('');
}

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});


//overlay

$(document).on('click', '.overlay', function() {
    noti.hide();
	popup.hide();
});

$(document).on('click', '.noti .confirm', function() {
    noti.hide();
	popup.hide();
})



// quick_submit

function quick_submit() {

}

function quick_input_add() {
	$('#quick_input_list').append('<input class="sub_input" id="quick_product"><input class="sub_input" id="quick_price"><input class="sub_input" id="quick_quantity">');
}

function quick_input_set() {
	quick_input_add();
}

// submit  서버와 통신하는 펑션들

function detail_submit() {
	console.log('a');
	frm = $('#sub_table_form');
	url = $(frm).attr('target');
	item_table = $('#item_list_table tr');

	// var form_data = $('form').serializeArray();
		item_data = $('#item_table').tableToJSON({
			ignoreColumns: [0,6],
			ignoreEmptyRows: true
		});
	item_data.shift();
	var pk = $('.table_highlight').attr('id').split('_')[1];

	// data = JSON.stringify(form_data) + "ordered_item_list:" + JSON.stringify(item_data);



	$.ajax({
        url: $(frm).attr('target'),
        cache: false,
        method: "POST",
		 data:JSON.stringify({
			 order_pk:pk,
			order_total_amount:de_commas($('#detail_table #order_total_amount').val()),
			order_paid_amount:de_commas($('#detail_table #order_paid_amount').val()),
			order_discounted_amount:de_commas($('#detail_table #order_discounted_amount').val()),
			order_outstanding_amount:de_commas($('#detail_table #order_outstanding_amount').val()),
			order_notes:de_commas($('#detail_table #adjustment_notes').val()),
			// order_store:$('#company_code').val(),
			 order_store_code : 2,
			// ordered_item_list:[
			// 	{"ordered_item":"15","ordered_item_item":"3","ordered_item_unit":"1","ordered_item_grade":"1","ordered_item_unit_price":"1000","ordered_item_qty":"10","ordered_item_description":"기존 오더 아이템 id=15"},
			// 	{"ordered_item":"15","ordered_item_item":"3","ordered_item_unit":"1","ordered_item_grade":"1","ordered_item_unit_price":"1000","ordered_item_qty":"10","ordered_item_description":"기존 오더 아이템 id=15"},
			// 	{"ordered_item":"15","ordered_item_item":"3","ordered_item_unit":"1","ordered_item_grade":"1","ordered_item_unit_price":"1000","ordered_item_qty":"10","ordered_item_description":"기존 오더 아이템 id=15"}
			// ],
			 ordered_item_list : item_data,

			datepicker_start:"2016/07/01",
			datepicker_end:"2016/07/03",
			search_store:""



		}),


        csrfmiddlewaretoken: '{{ csrf_token }}'
    })
    .done(function(msg) {
		//No Item list : order item 이 하나도 지adsfasdf정 안되었을경우 return값, order는 update된다. 
		//Product DoesNotExist : 등록시도하는 상품 없음, 
		//SomeError : 알수 없는 에러 발생,  refresh or db로 부터 다시 data를 읽어와서 data정합성을 맞춘다.
		//Order DoesNotExist : 잘못된 order id가 넘어옴. 

		//msg.total_outstanding_amount1  => 정정당당 현재까지 미수금
		//msg.total_outstanding_amount2  => 현재까지 전체 미수금

        alert("Data Saved : " + msg.result);
    })
    .fail(function() {
        noti.show("confirm","전송오류","전송이 실패했습니다. 같은 문제가 반복적으로 발생될 경우 고객센터로 문의바랍니다.");
		// location.reload(true);
		setTimeout(function () {
			// window.location.reload(true);
		},5000);
    })
}

// order_table


function detail_calc() {
	total = $('.item_total');
	total_price = Number('0');
	for(i=0;i<total.length;i++) {
		total_price = total_price + Number(de_commas($(total[i]).text()));
		}
	
	collect = de_commas($('#detail_table .collect').val());
	if (collect==0) {
		$('#detail_table .collect').val(0);
	}
	deduct = de_commas($('#detail_table .deduct').val());
	if (deduct==0) {
		$('#detail_table .deduct').val(0);
	}

	$('#detail_table .amount').val(commas(total_price));
	
	current_unconsumed = total_price - collect - deduct;
	
	$('#detail_table .unconsumed').val(commas(current_unconsumed));
	
	if(current_unconsumed < 1) {
		$('#detail_table .status').text('수금완료');
	}
}


function order_button_reset() {
	$('#new_order').html('새발주<span class="mdl-button__ripple-container"><span class="mdl-ripple is-animating" style="width: 149.714px; height: 149.714px; transform: translate(-50%, -50%) translate(30px, 7px);"></span></span>');
	$('#new_order').removeClass('progress');
}

function progress_start() {
	$('.progress').show();
}

function detail_init() {
	$('.detail_table').val('');
}

function detail_close() {
	detail_init();
	$('.table_highlight').removeClass('table_highlight');
	$('#sub_table').hide();

}

function item_list_table_init() {
	$('#item_list_table tr').remove();
}

function detail_new() {
	detail_init();
	item_list_table_init()
	$('#sub_table').show();
}

function detail_open(date,code,kind,amount,collect,deduct,unconsumed,note, status) {
	item_list_table_init();
	item_list = $('.table_highlight .item_list span');
	for(i=0;i<item_list.length;i++) {
		var item_data = $(item_list[i]).text().split(',');
		var item_no = $(item_list[i]).attr('data-itemcode');
		var item_grade = $(item_list[i]).attr('data-itemgrade');
		var item_unit = $(item_list[i]).attr('data-itemunit');
		var i_reverse = item_list.length - i;

		$('#item_list_table').append('<tr data-numb="'+ i_reverse +'"><td><label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect mdl-data-table__select" for="sub_row'+i_reverse+'"><input type="checkbox" id="sub_row'+ i_reverse +'" class="mdl-checkbox__input" /></label></td><td data-override="'+item_no+'">'+item_data[0]+'</td><td data-override="'+item_grade+'">'+item_data[1]+'</td><td data-override="'+item_unit+'">'+item_data[2]+'</td><td>'+commas(item_data[3])+'</td><td>'+commas(item_data[4])+'</td><td class="item_total">'+commas(item_data[5])+'</td></tr>');

		var table = document.querySelector('#sub_table');
		var headerCheckbox = table.querySelector('thead .mdl-data-table__select input');
		var boxes = table.querySelectorAll('tbody .mdl-data-table__select');
		var headerCheckHandler = function(event) {
			if (event.target.checked) {
				for (var i = 0, length = boxes.length; i < length; i++) {
					boxes[i].MaterialCheckbox.check();
				}
			} else {
				for (var i = 0, length = boxes.length; i < length; i++) {
					boxes[i].MaterialCheckbox.uncheck();
				}
			}
		};
		headerCheckbox.addEventListener('change', headerCheckHandler);
		componentHandler.upgradeDom();
	}
	

	$('#sub_table .date').val(date);
	$('#sub_table .code').val(code);
	// kind로 데이터 오류검사
	$('#sub_table .amount').val(commas(amount));
	$('#sub_table .collect').val(commas(collect));			
	$('#sub_table .deduct').val(commas(deduct));			
	$('#sub_table .unconsumed').val(commas(unconsumed));					
	$('#sub_table .note').val(note);				
	$('#sub_table .status').text(status);
	
	
	$('#sub_table').show();
	

}



// 아이템 테이블

$(document).on("click", ".add_item", function() {
	var add_id = $(this).parent().attr('id');

	switch (add_id) {
		case 'ui-id-1' :
			console.log('id는 1');
			break;
		case 'ui-id-2' :
			console.log('id는 2');
			break;
		case 'ui-id-3' : //품목추가
			popup.show('item_control');
			break;
		case 'ui-id-4' :
			console.log('id는 4');
			break;
		case 'ui-id-5' :
			console.log('id는 5');
			break;
		case 'ui-id-6' :
			console.log('id는 6');
			break;
	}

});

function detail_item() {

}

function detail_save(date,code,kind,amount,collect,deduct,unconsumed,note, status) {
	item_list = $('#item_list_table tr');
	item_list_td = [];
	items = "";
	for(var i = 0 ;i < item_list.length; i++) {
		item_list_td[i] = $(item_list[i]).find('td');
		var data_itemcode = $(item_list_td[i][1]).attr('data-override');
		var data_itemgrade = $(item_list_td[i][2]).attr('data-override');
		var data_itemunit = $(item_list_td[i][3]).attr('data-override');
		var item_item = $(item_list_td[i][1]).text();
		var item_grade = $(item_list_td[i][2]).text();
		var item_unit= $(item_list_td[i][3]).text();
		var item_unit_price = $(item_list_td[i][4]).text();
		var item_qty = $(item_list_td[i][5]).text();
		var item_total = $(item_list_td[i][6]).text();

		items = items + '<span data-itemcode="'+data_itemcode+'" data-itemgrade="'+data_itemgrade+'" data-itemunit="'+data_itemunit+'">'+item_item+','+item_grade+','+item_unit+','+de_commas(item_unit_price)+','+item_qty+','+de_commas(item_total)+'</span>';
		console.log(items);
	}

	// submit('sub_table_form');
	detail_submit();

	$('.table_highlight .date').text(date);
	$('.table_highlight .code').text(code);
	$('.table_highlight .kind').text(kind);
	$('.table_highlight .amount').text(commas(amount));
	$('.table_highlight .collect').text(commas(collect));				
	$('.table_highlight .deduct').text(commas(deduct));
	$('.table_highlight .unconsumed').text(commas(unconsumed));
	$('.table_highlight .note').text(note);
	$('.table_highlight .item_list').html(items);
	if(unconsumed < 1) {
		$('.table_highlight').removeClass('pending');
		$('.table_highlight').addClass('complete');
	}
	else {
		$('.table_highlight').addClass('pending');
		$('.table_highlight').removeClass('complete');
		
	}

	
/* 	$('.table_highlight .status').text(status); */				
}
function input_init() {
    	 	$('#product_code input').val('');
    	 	$('#product_grade input').val('');
    	 	$('#product_unit input').val('');
    	 	$('#product_price input').val('');
    	 	$('#product_quantity input').val('');
    	 	$('#product_amount input').val('');
    	 	$('#product_code input').focus();    	 	
}

function quick_code_set() {
	if(event.keyCode == 13)
    	 {
				 quick_input_set();
		  }
}

function set_company() {
    if(event.keyCode == 13)
        {
            $('#product_code input').focus();
        }
           
}

function set_today() {
    if(event.keyCode == 13)
        {
            if($('#order_date').val() == '')
                {
                    $('.today').val(today);
                }
                
            $('#company_code').focus();
        }
}


function enterTab(e) {

	if(event.keyCode == 13)
    	 {
			 e.preventDefault();
				 var inputs = $('.focus').closest('tr').find(':input');
				 inputs.eq( inputs.index($('.focus'))+ 1 ).focus();
		  }
}

function enterKeySubmit(e) {
	e.preventDefault();
	if(event.keyCode == 13)
    	 {
    	 	var code = $('#product_code input').val();
			var code_code = parseInt(code.match(/\(([^)]+)\)/)[1]);
    	 	var grade = $('#product_grade input').val();
			var grade_code = parseInt(grade.match(/\(([^)]+)\)/)[1]);
    	 	var unit = $('#product_unit input').val();
			var unit_code = parseInt(unit.match(/\(([^)]+)\)/)[1]);
    	 	var price = $('#product_price input').val();
    	 	var quantity = $('#product_quantity input').val();
    	 	var amount = $('#product_amount input').val();
			 var i_reverse = $('#item_list_table').find('tr:first').attr('data-numb');
			 console.log(i_reverse);
			 if(i_reverse == undefined) {

				 i_reverse = 1;
				 console.log(i_reverse);
			 }
			 else {
				 i_reverse = Number(i_reverse) + 1;
			 }

			 // 몇번째 줄인지 확인해야
			 $('#item_table > tbody:first').prepend('<tr data-numb="'+ i_reverse +'"><td><label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect mdl-data-table__select" for="sub_row'+ i_reverse +'"><input type="checkbox" id="sub_row'+ i_reverse +'" class="mdl-checkbox__input" /></label></td><td data-override="'+code_code+'">'+code+'</td><td data-override="'+grade_code+'">'+grade+'</td><td data-override="'+unit_code+'">'+unit+'</td><td>'+commas(price)+'</td><td>'+quantity+'</td><td class="item_total">'+commas(amount)+'</td></tr>');
			 input_init();  
			 detail_calc();
			 componentHandler.upgradeDom();

			 var table = document.querySelector('#sub_table');
			 var headerCheckbox = table.querySelector('thead .mdl-data-table__select input');
			 var boxes = table.querySelectorAll('tbody .mdl-data-table__select');
			 var headerCheckHandler = function(event) {
				 if (event.target.checked) {
					 for (var i = 0, length = boxes.length; i < length; i++) {
						 boxes[i].MaterialCheckbox.check();
					 }
				 } else {
					 for (var i = 0, length = boxes.length; i < length; i++) {
						 boxes[i].MaterialCheckbox.uncheck();
					 }
				 }
			 };
			 headerCheckbox.addEventListener('change', headerCheckHandler);
		  }
}

function calculate_open() {
	$('#calculate').show();
}



$('.overlay').on('click', function() {
    console.log('omg');
});


var page_init = {
	status : "failed",

	init: function() {
		console.log('init!!!');
		load('#item_control_wrapper','item_control');
	}
};

var board = {
	status : "show",

	show: function() {
		$('.board').show();
	},

	hide: function() {
		$('.board').hide();
	}
};

var add = {
	status : "waiting",

}

var noti = { // alert 대체
    status : "off",
    overlay : document.getElementsByClassName('overlay'),
    window : document.getElementsByClassName('noti'),
    
    init: function () {

    },
    
    show: function(type, title, msg) {
        $(noti.overlay).css('opacity', '0.7');
        $(noti.overlay).css('z-index', '999');
        $(noti.window).css('opacity', '1');

		switch(type) {
			case alert:
				$('.noti .title').text(title);
				$('.noti .msg .text').text(msg);
				$('.noti .action').find('.'+type).addClass('noti_show');
				break;

			default:
				$.ajax({
					url: type,
					cache: false,
					method: "GET"
				})
					.done(function(data) {
						// alert("Data Loaded : " + msg);
						$('.noti .title').text(title);
						$('.noti .msg .text').html(data);
						$('.noti .action').find('.save').addClass('noti_show');


					})
					.fail(function() {
						alert("failed");
					});

		}
    },
    
    hide: function() {
        $(noti.overlay).css('opacity', '0');
        $(noti.overlay).css('z-index', '0');
        $('.noti .action').find('.noti_show').removeClass('noti_show');
        $(noti.window).css('opacity', '0');        
    }
};


var popup = {
	status : "off",
	overlay : document.getElementsByClassName('overlay'),
	window : document.getElementsByClassName('popup'),

	init: function () {

	},

	show: function(url, v) {
		$(popup.overlay).css('opacity', '0.7');
		$(popup.overlay).css('z-index', '999');
		$(popup.window).css('opacity', '1');

		switch(url) {
			case alert:
				$('.popup .msg .text').text(data);
				// $('.popup .action').find('.'+type).addClass('popup_show');
				break;

			default:
				$.ajax({
					url: url,
					cache: false,
					method: "GET"
				})
					.done(function(data) {
						// alert("Data Loaded : " + msg);
						$('.popup .msg').html(data);
						// $('.popup .action').find('.save').addClass('popup_show');


					})
					.fail(function() {
						alert("failed");
					});

		}
	},

	hide: function() {
		$(popup.overlay).css('opacity', '0');
		$(popup.overlay).css('z-index', '0');
		$('.popup .action').find('.popup_show').removeClass('popup_show');
		$(popup.window).css('opacity', '0');
	}
};


var detail = {
	status : "hide",

	init: function() {

	},

};


var order = {
    id:"1",
    status:"unfold",
    
    init: function () {
        $('[data-role="order"] [data-role="value"]').text('');
    },
    
    get: function() {
        $.ajax({
            url: "/submit_order",
            cache: false,
            method: "GET"
        })
        .done(function(msg) {
            alert("Data Loaded : " + msg);
        })
        .fail(function() {
            alert("failed");
        });
    },
    
    fold: function(callback) {
        $('#order_table tbody').attr('style', 'height:200px');
        setTimeout(function() {
            var scroll_id_char = $('.table_highlight').attr('id');
			var tr_index = $("#order_table_tbody > tr").index($("#order_table_tbody > tr.table_highlight"));
            $('#order_table_tbody').scrollTop(tr_index * 40 );
        }, 310);
        order.status = 'fold';
        
        if (typeof callback === "function") {
            callback();
        }   
        
    },
    
    unfold: function(callback) {
        $('#order_table tbody').css('height', '600px');
        
        order.status = 'unfold';
        
        if (typeof callback === "function") {
            callback();
        }   

    }
    
};

$(document).ready(function() {
	var table = document.querySelector('#order_table');
	var headerCheckbox = table.querySelector('thead .mdl-data-table__select input');
	var boxes = table.querySelectorAll('tbody .mdl-data-table__select');
	var headerCheckHandler = function(event) {
		if (event.target.checked) {
			for (var i = 0, length = boxes.length; i < length; i++) {
				boxes[i].MaterialCheckbox.check();
			}
		} else {
			for (var i = 0, length = boxes.length; i < length; i++) {
				boxes[i].MaterialCheckbox.uncheck();
			}
		}
	};
	headerCheckbox.addEventListener('change', headerCheckHandler);

	page_init.init();

	$('#sub_remove').on("click", function() {
		$('tbody .is-checked').parent().parent().remove();
		console.log('remove!');
	});

	$('.quick_code_set').on("click", function() {
		quick_input_set();
	});

	$('#detail_table input').on("change", function() {
		detail_calc();
	});

	$('#detail_table input').on("focusin", function() {
		$(this).val(''+de_commas($(this).val()));
	});

	$('#detail_table input').on("focusout", function() {
		$(this).val(''+commas($(this).val()));
	});
	
	$('input').on("focusin", function() {
		$(this).addClass('focus');
	});

	$('input').on("focusout", function() {
		$(this).removeClass('focus');
	});


	$('#product_amount_input').on("focusin", function() {
		price = $('#product_price_input').val();

		quantity = $('#product_quantity_input').val();

		amount = price * quantity;

		$('#product_amount_input').val(amount);
	});

// user menu
	$('#user_logout').on("click", function() {
		alert('안돼 안시켜줘. 돌아가');
	});
    
// datepicker init
    $('#datepicker').datepicker();
    
    $('#quick_submit').on("click", function() {
	   quick_submit(); 
    });
    
// table toggle
//     $(document).on("click", ".order_list td", function() {
//         if (order.status == "writing") {
//             console.log("writing");
//         }
//         else if ($(this).parent().hasClass('table_highlight')) {
// 		detail_close();
// 		order.unfold();
//         }
//         else {
// 			detail_close();
//             $(this).parent().addClass('table_highlight');
//             date = $(this).parent().find('.date').text();
//             code = $(this).parent().find('.code').text();
// 			kind = $(this).parent().find('.kind').text();
// 			amount = $(this).parent().find('.amount').text();
// 			collect = $(this).parent().find('.collect').text();
// 			deduct = $(this).parent().find('.deduct').text();
// 			unconsumed = $(this).parent().find('.unconsumed').text();
// 			note = $(this).parent().find('.note').text();
// 			status = '수금대기';
// 			if($(this).parent().hasClass('complete')) {
// 				status = '수금완료';
// 			}
//
//             detail_open(date,code,kind,amount,collect,deduct,unconsumed,note,status);
//             if(order.status == 'unfold') {
//                 order.fold();
//             }
//         }
//     });

	$(document).on("click", "tr.order_list", function() {
		if (order.status == "writing") {
			console.log("writing");
		}
		else if ($(this).hasClass('table_highlight')) {
			detail_close();
			order.unfold();
		}
		else {
			detail_close();
			$(this).addClass('table_highlight');
			date = $(this).find('.date').text();
			code = $(this).find('.code').text();
			kind = $(this).find('.kind').text();
			amount = $(this).find('.amount').text();
			collect = $(this).find('.collect').text();
			deduct = $(this).find('.deduct').text();
			unconsumed = $(this).find('.unconsumed').text();
			note = $(this).find('.note').text();
			status = '수금대기';
			if($(this).hasClass('complete')) {
				status = '수금완료';
			}

			detail_open(date,code,kind,amount,collect,deduct,unconsumed,note,status);
			if(order.status == 'unfold') {
				order.fold();
			}
		}
	});
    
    $('.garak_drawer').html("<span>Garak</span><span>Tool</span>");
    
// new order
    $('#new_order').on("click", function() { // 새발주
		var data_numb = Number($('#order_table_tbody tr:first').attr('data-numb')) + 1;

    	if($(this).hasClass('progress')) {
	    	alert('하던거나 마저 입력하삼');	
    	}
    	else {
    	detail_close();
    	$(this).addClass('progress');
    	$('#new_order').html('입력중<span>.</span><span>.</span><span>.</span>');
        $('#order_table > tbody:first').prepend('<tr data-role="order" data-numb="'+ data_numb +'" class="order_list table_highlight" id="order_"><td><label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect mdl-data-table__select mdl-js-ripple-effect--ignore-events" for="row['+ data_numb +']"><input id="row['+ data_numb +']"type="checkbox" class="mdl-checkbox__input"></label></td><td class="date"></td><td class="code"></td><td class="kind"></td><td class="amount"></td><td class="collect"></td><td class="deduct"></td><td class="unconsumed"></td><td class="note last_column"></td></tr>');
        detail_new();
		$('.order_progress').show();        
// 		input_init();
//         $('#order_date').focus();
// 		$('.today').val(today);
		$('.today').attr('placeholder', today);
        order.fold();

			componentHandler.upgradeDom();


			var table = document.querySelector('#main_table');
			var headerCheckbox = table.querySelector('thead .mdl-data-table__select input');
			var boxes = table.querySelectorAll('tbody .mdl-data-table__select');
			var headerCheckHandler = function(event) {
				if (event.target.checked) {
					for (var i = 0, length = boxes.length; i < length; i++) {
						boxes[i].MaterialCheckbox.check();
					}
				} else {
					for (var i = 0, length = boxes.length; i < length; i++) {
						boxes[i].MaterialCheckbox.uncheck();
					}
				}
			};
			headerCheckbox.addEventListener('change', headerCheckHandler);
        
        
        setTimeout(function() {
            $('#order_date').focus();
            order.status = "writing";
        }, 450);

		}
    });

//    $('#new_order').on("click", function() { // 새발주
//        $('#order_table > tbody:first').prepend('<tr class="order_list"><td><label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect mdl-data-table__select mdl-js-ripple-effect--ignore-events is-upgraded" data-upgraded=",MaterialCheckbox,MaterialRipple"><input type="checkbox" class="mdl-checkbox__input"><span class="mdl-checkbox__focus-helper"></span><span class="mdl-checkbox__box-outline"><span class="mdl-checkbox__tick-outline"></span></span><span class="mdl-checkbox__ripple-container mdl-js-ripple-effect mdl-ripple--center" data-upgraded=",MaterialRipple"><span class="mdl-ripple"></span></span></label></td><td>2015-08-02</td><td>정정당당(001)</td><td>배추(001)</td><td>165,000</td><td>65,000</td><td>0</td><td>100,000</td><td class="last_column">0</td></tr>');
  //  });

    
    $('#new_item').on("click", function() {
    	code = $('#product_code input').val();
    	grade = $('#product_grade input').val();
    	unit = $('#product_unit input').val();
    	price = $('#product_price input').val();
    	quantity = $('#product_quantity input').val();
    	amount = price*quantity;
    	$('.input_section').show();
    	input_init();
/*     	amount = $('#product_amount input').val(); */
    
        
    });
  
  
  $('#detail_confirm').on("click", function(e) {
	  		e.preventDefault();
	        date = $('#sub_table .date').val();
            code = $('#sub_table .code').val();
			kind = $('#item_table tr').length - 2;
			amount = $('#sub_table .amount').val();
			collect = $('#sub_table .collect').val();
			deduct = $('#sub_table .deduct').val();
			unconsumed = $('#sub_table .unconsumed').val();
			note = $('#sub_table .note').val();
			status = $('#sub_table .status').text();

	  		detail_save(date,code,kind,amount,collect,deduct,unconsumed,note, status);
			$('.order_progress').hide();
			order.status = "fold";



			
			// if (confirm('세이브 하시면 후회하실텐데, 그래도 세이브 하시겠어요?')) {
			// 	alert('세이브 되었습니다.');
			// 	detail_save(date,code,kind,amount,collect,deduct,unconsumed,note, status);
			// 	$('.order_progress').hide();
			// 	order_button_reset();
			// 	order.status = "fold";
			// } else {
			// 	alert('취소했지만 세이브 되었습니다.');
			// }

  });

  $('#detail_cancel').on("click", function(e) {
	  e.preventDefault();
	  $('.table_highlight').remove();
	  detail_close();
	  $('.order_progress').hide();
	  order_button_reset();
	  order.unfold();

	  // if (confirm('작성한 내용이 다 삭제됩니다. 취소 하시겠습니까?')) {
		// 		$('.table_highlight').remove();
		// 		detail_close();
		// 		$('.order_progress').hide();
		// 		order_button_reset();
		// 		order.unfold();
		// 	} else {
		// 		alert('취소를 취소하셨지만 취소 버튼을 누르셨으니 취소하겠습니다. 작성한 내용 다 삭제되지롱');
		// 	}
	  
  });
    
// new product
    
    
    $('#new_calculate').on("click", function() {
	    pending_list = $('.pending');
		$(pending_list[0]).find('.code').text();
		for (var i in pending_list) {
			console.log(pending_list[i]);
		}
    
    
    	$('.calculate_overlay').show();
    	calculate_open();

	   $('.calculate_progress').show(); 
    });
    
    $('#deduct').on("click", function() {
	    alert('공제는 거절한다.');
    });

    $('#unconsumed').on("click", function() {
	    alert('안돼. 미수 안해줘. 돌아가.');
    });
    
    $('.calculate_overlay').on("click", function() {
	   $('.calculate_overlay').hide();
	   $('#calculate').hide(); 
	   $('.calculate_progress').hide(); 
    });


    
    
    
});

