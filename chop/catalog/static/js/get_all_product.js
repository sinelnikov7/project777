function get_all_product(event){
    console.log(how_many)
    let root_all_product = document.getElementById('content')
    let all_product_url = `/api/product`
    let filter = event.target.id

    if(how_many < 1){
    console.log("Превый")
        how_many += 1
        filter = event.target.id
        let all_product_url = get_url_product(filter)
        fetch(all_product_url).then((response)=>response.json()).then((product)=>{

                let html = `<div style="width:100%; height:1px; clear:both;"></div>
                <div id="category_animal"></div>
                <div class="catalog_title">
                        <div class="pop_tov_h2"><h1 class="empty">Каталог товаров для категории </h1>
                        <div style="display:flex; align-items: center;" >
                         <label>Сортировать по:</label>
                         <select>
                          <option>Новизне</option>
                          <option>Популярности</option>
                          <option>Названию "От А до Я"</option>
                          <option>Названию "От Я до А"</option>
                          <option>Цене по возрастанию</option>
                          <option>Цене по убыванию</option>
                        </select>
                        <img class="" src="static/img/rebote_filter.jpg" title="Сбросить фильтр" style="cursor:pointer;" onClick="get_all_product(event)">
                        </div>
                     </div>
                    </div>
                    <div class="page_cat">
                        <div class="filters">
                            <div class="filters_radio" id="radio">
                            </div>
                            <div class="filters_check-box" id="check-box">
                            </div>
                        </div>
                        <div class="products" id="products">`

    html += get_product_div(product, html)
     html += `</div>`
    root_all_product.innerHTML = html
    get_categories()
    get_filter_radio()
    get_filter_check_box()
})

    }else if(how_many > 0){
    console.log("Второй")
    let root_all_product_div = document.getElementById('products')
    how_many += 1
    let all_product_url = `/api/product/?${filter}`
    fetch(all_product_url).then((response)=>response.json()).then((product)=>{
    html = get_product_div(product, html)
    root_all_product_div.innerHTML = html
})
}
}

function get_filter_radio(){
    fetch(`/api/product_category`).then((response)=>response.json()).then((product_category)=>{
        let root_radio = document.getElementById('radio')
        let html_radio =
        `<strong>Тип товара</strong><br><br>
            <form>
            `
            for(let i in product_category.results){
            html_radio += `<input type="radio" value="value1" name="group1"><label>${product_category.results[i].name}</label><br><br>`
            }
            html_radio += `
            </form>`
            root_radio.innerHTML = html_radio
            })
}

function get_filter_check_box(){
    fetch(`/api/brand`).then((response)=>response.json()).then((brand)=>{
        let root_check_box = document.getElementById('check-box')
        let html_check_box =
        `<strong>Брэнд</strong><br><br>
            <form>
            `
            for(let i in brand.results){
            html_check_box += `<input type="checkbox" id="scales" name="scales" unchecked>
            <label>${brand.results[i].name}</label><br><br>`
            }
            html_check_box += `
            <button class="myButton">Найти</button>
            </form>`
            root_check_box.innerHTML = html_check_box
            })
}

function get_url_product(filter){
    console.log(filter, "То что приходит")
    if(filter.length < 1){
        url = `/api/product`
        console.log(url,"УРЛ")
    return url
    }else if(filter.length > 1){
        url = `/api/product/?${filter}`
        console.log(url,"УРЛ")
    return url
    }
}