$(document).ready(function(){
    console.log("starting jquery::::::::::::::::::")
    $('#search').on('click',function(){
        // alert("searching.....")
        var sku = $('#sku-val').val();
        getProducts(sku)
        // getIdx(sku)
    })

    function getProducts(sku){
        console.log("searching............")
         var url = '/recommendations/'+sku
        
        console.log("fetching recommended products ..."+url)
        $.getJSON(url,function(data){
            console.log('products :',data)
            showIdx(data[0])
            showProducts(data)
             })
    }
     
    function showProducts(data){
        var html =  "<table> <tr>"
        $.each(data.slice(1,6), function(i, d) {
            html = html + `<td><div class="square">
            <img src=https://`+d.image+`>
            <p>SKU : `+d.sku+`</p>
            
            <p>Price : `+d.price+`</p>
            <input type="button" class="btn btn-primary" onclick=" window.open('`+d.link+`', '_blank'); return false;" value="Know More" />
            </div></td>`
        }
        );
        
        html = html + `</tr></table>`
        console.log(html)
        document.getElementById("recommendations").innerHTML = html;
    }

    function showIdx(d){
        var htmlidx =  " "

            console.log(d)
            htmlidx = htmlidx + `<div class="square" style="padding:0px; margin:0px;">
            
            <img src=https://`+d.image+`>
            <p>SKU : `+d.sku+`</p>
            <p>Price : `+d.price+` &nbsp; <input type="button" class="btn btn-primary" onclick=" window.open('`+d.link+`', '_blank'); return false;" value="Know More" /> </p>            
            
            
            </div>`
        
    
        console.log(htmlidx)
        document.getElementById("idxImage").innerHTML = htmlidx;
    }

})