$('.member-search').on('click',function(){
    var searchkey=$('input[name=searchKey]').val();
    if(searchkey!=' ' && searchkey.length > 4){
        $.ajax({
            url :"/members?filter="+searchkey,
            dataType : 'json',
            success: function(result){
                var table=memberSearchResult(result);
                $('#tableData').html(table);
            },
            error: function(){
                // TODO : Do something if ajax gave error response
            }
        });
    }
});

//$('.inner-search').on('keyup',function(){
//    var searchkey=$('input[name=innerSearchKey]').val();
//    if(searchkey!=' ' && searchkey.length > 4){
//        $.ajax({
//            url :"/members?filter="+searchkey,
//            dataType : 'json',
//            success: function(result){
//                // Collection of data for this app is subscriptions
//                app.collection = new MemberCollection(result);
//                app.membersHome();
//                console.log(app.collection);
//
//                var table=memberSearchResult(result);
//                $('#tableData').html(table);
//            },
//            error: function(){
//                // TODO : Do something if ajax gave error response
//            }
//        });
//    }
//});
$('.inner-search').on('click',function(){
    var searchKey= $.trim($('input[name=innerSearchKey]').val());
    if(searchKey.length >3){
        app.collection=new MemberCollection();
        app.collection.url="/members?filter="+searchKey;
        app.collection.fetch({
            success : function(){
                app.membersHome();
            },
            error:function(){
                console.log("Error..................!");
            }
        });
    }
});

function memberSearchResult(data)
{
    var table='<table border="0" cellpadding="10">';
    for (var i=0, size=data.length; i<size; i++){
        if(i%3==0){
            table+='<tr><td valign="top" class="btn member-information">';
            if(data[i].photo){
                table+='<img src='+data[i].photo+' width="100px" height="100px" alt="image"/>';
            }else{
                table+='<img src="/img/user.jpg" width="100px" height="100px" alt="image"/>';
            }
            table+=data[i].name+'<br/>'+data[i].email+'<br/>';
            if(data[i].mobile != null){
                table+=data[i].mobile+'<br/>';
            }
            table+='<input type="hidden" name="memberId" value='+data[i].id+'/>';
            table+='</td>';
        }else{
            table+='<td valign="top" class="btn member-information">';
            if(data[i].photo){
                table+='<img src='+data[i].photo+' width="100px" height="100px" alt="image"/>';
            }else{
                table+='<img src="/img/user.jpg" width="100px" height="100px" alt="image"/>';
            }
            table+=data[i].name+'<br/>'+data[i].email+'<br/>';
            if(data[i].mobile != null){
                table+=data[i].mobile+'<br/>';
            }
            table+='<input type="hidden" name="memberId" value='+data[i].id+'/>';
            table+='</td>';
        }
    }
    table+='</tr>';

    return table;
}

//// Below code is not working now
//
//$('document').ready(function(){
//    disaMember.init();
//});
//
//disaMember.init = function()
//{
//    // to search member information
//    $('.member-search').on('keyup',this.member.search.memberSearch);
//
//    $("input[name='otherOccasion']").hide();
//    $("select[name='Occasion']").on('change',this.member.occasion.otherOccasion);
//    $("input[name='sevainthenameofcheckbox']").on('click',this.member.sevaIntheNameOf.inTheNameOf);
//};
//
//disaMember.member = {
//
//    /**
//     * To search member with the information of member name,sur name,email,phone or mobile
//     */
//    search : {
//        memberSearch : function(){
//            var searchkey=$('input[name=searchKey]').val();
//            $.ajax({
//                url :"/members?filter="+searchkey,
//                dataType : 'json',
//                success: function(result){
//                    return result;
//                },
//                error: function(){
//                    // TODO : Do something if ajax gave error response
//                }
//            });
//        }
//    },
//
//    occasion : {
//        /**
//         * If Occasion is other then showen the input field
//         */
//        otherOccasion : function(){
//            var occasion=$("select[name='Occasion']").val();
//            if(occasion=='others'){
//                $("input[name='otherOccasion']").show();
//            }else{
//                $("input[name='otherOccasion']").hide();
//            };
//        }
//    },
//    /**
//     * If donor is not in that seva
//     */
//    sevaIntheNameOf :{
//        inTheNameOf : function(){
//            var sevainthenameofcheckbox= $("input[name='sevainthenameofcheckbox']").val();
//            if(sevainthenameofcheckbox != 'notDonor'){
//                $("input[name='sevainthenameof']").removeAttr("readonly");
//            }else{
//                $("input[name='sevainthenameof']").attr("readonly","readonly");
//            }
//        }
//    }
//};
//
