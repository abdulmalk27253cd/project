let filterarray = []

let galleryarray = [
    {
        id: 1,
        name: "USB K",
        src: "./gg.jpg",
        price: "100 AED"
    },
    {
        id: 2,
        name: "MK",
        src: "./gg.jpg",
        price: "20 AED"
    },
    {
        id: 3,
        name: "GG",
        src: "./gg.jpg",
        price: "30 AED"
    },
    {
        id: 4,
        name: "AA",
        src: "./gg.jpg",
        price: "40 AED"
    },
]

function showgallery(currarray){

    document.getElementById("product").innerText = "";
    for(var i=0;i<currarray.length;i++){
        document.getElementById("product").innerHTML += `
                            <div class="product">
                        <h1>!</h1>
                        <div class="img">${currarray[i].src}</div>
                        <!-- pdetils -->
                        <div class="pdetils">
                            <h2>${currarray[i].name}</h2>
                            <p>${currarray[1].price}</p>
                        </div>
                    </div>
        `
    }

}



document.getElementById("searchInput").addEventListener("keyup",function(){
    let text = document.getElementById(searchInput).value;

    filterarray = galleryarray.filterarray.filter(function(a){
        if(a.name.includes(text)){
            return a.name;
        }
    });
    if(this.value ==""){
        showgallery(galleryarray);
    }
    else{
        if(filterarray == ""){
            document.getElementById("para").style.display = 'block';
            document.getElementById("product").innerHTML = "";
        }
        else{
            showgallery(filterarray);
            document.getElementById("para").style.display = 'none';   
        }
    }
})