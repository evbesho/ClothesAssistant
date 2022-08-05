let searchBar = document.getElementById("q");
let enter = document.getElementById("bt");
const userCardTemplate = document.querySelector("[data-user-template]");
const amazonContainer = document.querySelector("[amazon-container]");
const etsyContainer = document.querySelector("[etsy-container]");
var param = "";

document.addEventListener('keyup', (event) => {
    var name = event.key;
    if (name === 'Enter') {
      param = searchBar.value;
      console.log(param);
    //   window.location.href = "search";
      const items = document.querySelectorAll('.item');
      items.forEach(item => {
        item.remove();
      })
      myfunction(param);
    }
  }, false);

enter.addEventListener("click", p => {
    param = searchBar.value;
    console.log(param);
    // window.location.href = "search";
    const items = document.querySelectorAll(".item");
      items.forEach(item => {
        item.remove();
    })
    myfunction(param);
})

function myfunction(param){
    const out = {"param": param};
    const jay = JSON.stringify(out);
    console.log(jay);

    $.ajax({
        url: "/run",
        type: "POST",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(jay),
        success: function(results){
            results => results.json();
            console.log(results);

            var am = Object.keys(results[0]);
            for (i = 0; i < am.length; i++){
                const card = userCardTemplate.content.cloneNode(true).children[0];
                const name = card.querySelector("[name]");
                const link = card.querySelector("[link]");
                name.textContent = am[i];
                link.href = results[0][am[i]];
                link.target = "_blank";
//                link.document.getElementById('pic').src="css/images/highest.jpg";
                amazonContainer.append(card);
            }

            var et = Object.keys(results[1]);
            for (j = 0; j < et.length; j++){
                const card = userCardTemplate.content.cloneNode(true).children[0];
                const name = card.querySelector("[name]");
                const link = card.querySelector("[link]");
                name.textContent = et[j];
                link.href = results[1][et[j]];
                link.target = "_blank";
//                link.document.getElementById('pic').src="css/images/highest.jpg";
                etsyContainer.append(card);
            }

        }
    });
}

