function commas_checker(x) {
	console.log('요거 만들어야 할듯');
}

function commas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function de_commas(x) {
	return x.toString().split(',').join('');
}

function quick_submit() {
	
	
}


function quick_input_add() {
	$('#quick_input_list').append('<input class="sub_input" id="quick_product"><input class="sub_input" id="quick_price"><input class="sub_input" id="quick_quantity">');
}

function quick_input_set() {
	quick_input_add();
	
}

function detail_calc() {
	total = $('.item_total');
	total_price = Number('0');
	for(i=0;i<total.length;i++) {
		total_price = total_price + Number(de_commas($(total[i]).text()));
		console.log(total_price);
		}
	
	collect = de_commas($('#detail_table .collect').val());
	deduct = de_commas($('#detail_table .deduct').val());
		
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
		item_data = $(item_list[i]).text().split(',');
		console.log(item_data);
		$('#item_list_table').append('<tr><td><label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect mdl-data-table__select mdl-js-ripple-effect--ignore-events is-upgraded" data-upgraded=",MaterialCheckbox,MaterialRipple"><input type="checkbox" class="mdl-checkbox__input"><span class="mdl-checkbox__focus-helper"></span><span class="mdl-checkbox__box-outline"><span class="mdl-checkbox__tick-outline"></span></span><span class="mdl-checkbox__ripple-container mdl-js-ripple-effect mdl-ripple--center" data-upgraded=",MaterialRipple"><span class="mdl-ripple"></span></span></label></td><td>'+item_data[0]+'</td><td>'+item_data[1]+'</td><td>'+item_data[2]+'</td><td>'+commas(item_data[3])+'</td><td>'+commas(item_data[4])+'</td><td class="item_total">'+commas(item_data[5])+'</td></tr>');
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

function detail_save(date,code,kind,amount,collect,deduct,unconsumed,note, status) {
	$('.table_highlight .date').text(date);
	$('.table_highlight .code').text(code);
	$('.table_highlight .kind').text(kind);
	$('.table_highlight .amount').text(commas(amount));
	$('.table_highlight .collect').text(commas(collect));				
	$('.table_highlight .deduct').text(commas(deduct));
	$('.table_highlight .unconsumed').text(commas(unconsumed));
	$('.table_highlight .note').text(note);
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


function enterTab() {
	if(event.keyCode == 13)
    	 {
				 var inputs = $('.focus').closest('tr').find(':input');
				 inputs.eq( inputs.index($('.focus'))+ 1 ).focus();
		  }
}

function enterKeySubmit() {

	if(event.keyCode == 13)
    	 {
    	 	code = $('#product_code input').val();
    	 	grade = $('#product_grade input').val();
    	 	unit = $('#product_unit input').val();
    	 	price = $('#product_price input').val();
    	 	quantity = $('#product_quantity input').val();
    	 	amount = $('#product_amount input').val();
			 $('#item_table > tbody:first').prepend('<tr><td><label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect mdl-data-table__select mdl-js-ripple-effect--ignore-events is-upgraded" data-upgraded=",MaterialCheckbox,MaterialRipple"><input type="checkbox" class="mdl-checkbox__input"><span class="mdl-checkbox__focus-helper"></span><span class="mdl-checkbox__box-outline"><span class="mdl-checkbox__tick-outline"></span></span><span class="mdl-checkbox__ripple-container mdl-js-ripple-effect mdl-ripple--center" data-upgraded=",MaterialRipple"><span class="mdl-ripple"></span></span></label></td><td>'+code+'</td><td>'+grade+'</td><td>'+unit+'</td><td>'+commas(price)+'</td><td>'+quantity+'</td><td class="item_total">'+commas(amount)+'</td></tr>');    
			 input_init();  
			 detail_calc();
		  }
}

function calculate_open() {

	$('#calculate').show();
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


function submit(form) {
    url = "/submit_order";
	
	$.ajax({
        url: "/submit_order",
        cache: false,
        method: "POST",
		data:JSON.stringify({
			order_amount:"60000000",
			collect_money:"20000000",
			subtract_amount:"10000000",
			outstanding_amount:"30000000", 
			description:"봉수네 상회 일 껄",
			selling_partner:"2",
			order_pk:"1",
			order_item_list:[
				{"id":"2","product":"1","grade":"1등급","unit_price":"1000","amount":"10","description":"기존 오더 아이템 id=2"},
				{"id":"1","product":"2","grade":"2등급","unit_price":"2000","amount":"20","description":"기존 오더 아이템 id=1"},
				{"id":"","product":"6","grade":"별 세개","unit_price":"3000","amount":"30","description":"신규 오더 아이템"}
			]
		}),
        csrfmiddlewaretoken: '{{ csrf_token }}'
    })
    .done(function(msg) {
		//No Item list : order item 이 하나도 지정 안되었을경우 return값, order는 update된다. 
		//Product DoesNotExist : 등록시도하는 상품 없음, 
		//SomeError : 알수 없는 에러 발생,  refresh or db로 부터 다시 data를 읽어와서 data정합성을 맞춘다.
		//Order DoesNotExist : 잘못된 order id가 넘어옴. 
        alert("Data Saved : " + msg.result);
    })
    .fail(function() {
        alert("failed");
    });
}

$('.overlay').on('click', function() {
    console.log('omg');
});


var popup = {
    status : "off",
    overlay : document.getElementsByClassName('overlay'),
    window : document.getElementsByClassName('popup'),
    
    init: function () {

    },
    
    on: function(msg) {
        $(popup.overlay).css('opacity', '0.7');
        $(popup.overlay).css('z-index', '999');
        $(popup.window).css('top', '50%');
    },
    
    off: function() {
        $(popup.overlay).css('opacity', '0');
        $(popup.overlay).css('z-index', '9');
        $(popup.window).css('top', '-50%');        
    }
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
            $('#order_table_tbody').scrollTop(scroll_id_char.slice(-1) * 40 - 40);
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
		console.log(price);
		quantity = $('#product_quantity_input').val();
		console.log(quantity);
		amount = price * quantity;
		console.log(amount);
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
    $(document).on("click", ".order_list td", function() {
        if (order.status == "writing") {
            console.log("writing");
        } 
        else if ($(this).parent().hasClass('table_highlight')) {
		detail_close();
		order.unfold();
        }
        else {
			detail_close();
            $(this).parent().addClass('table_highlight');
            date = $(this).parent().find('.date').text();
            code = $(this).parent().find('.code').text();
			kind = $(this).parent().find('.kind').text();
			amount = $(this).parent().find('.amount').text();
			collect = $(this).parent().find('.collect').text();
			deduct = $(this).parent().find('.deduct').text();
			unconsumed = $(this).parent().find('.unconsumed').text();
			note = $(this).parent().find('.note').text();
			status = '수금대기';
			if($(this).parent().hasClass('complete')) {
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
    	if($(this).hasClass('progress')) {
	    	alert('하던거나 마저 입력하삼');	
    	}
    	else {
    	detail_close();
    	$(this).addClass('progress');
    	$('#new_order').html('입력중<span>.</span><span>.</span><span>.</span>');
        $('#order_table > tbody:first').prepend('<tr class="order_list table_highlight"><td><label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect mdl-data-table__select mdl-js-ripple-effect--ignore-events is-upgraded" data-upgraded=",MaterialCheckbox,MaterialRipple"><input type="checkbox" class="mdl-checkbox__input"><span class="mdl-checkbox__focus-helper"></span><span class="mdl-checkbox__box-outline"><span class="mdl-checkbox__tick-outline"></span></span><span class="mdl-checkbox__ripple-container mdl-js-ripple-effect mdl-ripple--center" data-upgraded=",MaterialRipple"><span class="mdl-ripple"></span></span></label></td><td class="date"></td><td class="code"></td><td class="kind"></td><td class="amount"></td><td class="collect"></td><td class="deduct"></td><td class="unconsumed"></td><td class="note last_column"></td></tr>');
        detail_new();
		$('.order_progress').show();        
// 		input_init();
//         $('#order_date').focus();
// 		$('.today').val(today);
		$('.today').attr('placeholder', today);
        order.fold();
        
        
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
  
  
  $('#detail_confirm').on("click", function() {
	        date = $('#sub_table .date').val();
            code = $('#sub_table .code').val();
			kind = $('#item_table tr').length - 2;
			amount = $('#sub_table .amount').val();
			collect = $('#sub_table .collect').val();
			deduct = $('#sub_table .deduct').val();
			unconsumed = $('#sub_table .unconsumed').val();
			note = $('#sub_table .note').val();
			status = $('#sub_table .status').text();
			
			
			if (confirm('세이브 하시면 후회하실텐데, 그래도 세이브 하시겠어요?')) {
				alert('세이브 되었습니다.');
				detail_save(date,code,kind,amount,collect,deduct,unconsumed,note, status);
				$('.order_progress').hide();
				order_button_reset();
				order.status = "fold";
			} else {
				alert('취소했지만 세이브 되었습니다.');
			}

  });

  $('#detail_cancel').on("click", function() {
			if (confirm('작성한 내용이 다 삭제됩니다. 취소 하시겠습니까?')) {
				$('.table_highlight').remove();
				detail_close();
				$('.order_progress').hide();
				order_button_reset();
				order.unfold();
			} else {
				alert('취소를 취소하셨지만 취소 버튼을 누르셨으니 취소하겠습니다. 작성한 내용 다 삭제되지롱');
			}
	  
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

