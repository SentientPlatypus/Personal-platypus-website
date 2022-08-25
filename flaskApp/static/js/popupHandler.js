function openThePopup(parentID) {
    console.log("OpenThePopup Called")
    let background = document.getElementById("background")
    let popup = document.getElementById("popup")
    let projectItem = document.getElementById(parentID)
    let popupData = projectItem.getElementsByClassName("popupData")[0]
    $(background).toggleClass("hidden")
    $(popup).toggleClass("hidden")
    while (popup.firstChild)
    {
        popup.removeChild(popup.firstChild);
    }
    console.log(popupData)
    console.log(popupData.children)
    for (const child in popupData.children)
    {
        console.log(popupData.children[child])
        popup.appendChild(popupData.children[child].cloneNode(true))
    }
}

function closeThePopup() {
    console.log("CloseThePopup Called")
    let background = document.getElementById("background")
    let popup = document.getElementById("popup")
    $(background).toggleClass("hidden")
    $(popup).toggleClass("hidden")
}