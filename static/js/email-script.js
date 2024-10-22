targetemail = 'info+'
targetdomain = '@mavisgroup.by'
domainname = 'https://mavisgroup.by/'

const getdomainName = (url) => url.replace(/^https?:\/\//, "")
    .replace(/^www\./, "")
    .replace(/\.[^.]*$/, '').replace('.', '').substr(0, 8);


// Тут меняем список мест где надо поменять
const places = () => {
    let contact_link, contact_link_text, footers
    contact_link = document.getElementsByClassName('email__header__tracking')[0]
    contact_link_text = document.getElementsByClassName('email__footer__tracking')[0]

    return [contact_link, contact_link_text]

}



const detection = () => {
    let parameters = Object
    let search = location.search.substring(1);

    if (getdomainName(document.referrer) != getdomainName(domainname)) {



        if (document.referrer == '' && !localStorage.getItem('ref')) {
            let historydata = []
            let search = location.search.substring(1);
            historydata.push('direct')
            if (search) {
                parameters = JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g, '":"') + '"}')
                historydata.push(parameters['utm_source']);
            }
            localStorage.setItem("ref", JSON.stringify(historydata))

        } else if (document.referrer != '' && !localStorage.getItem('ref')) {
            let historydata = []
            let search = location.search.substring(1);
            historydata.push(getdomainName(document.referrer))
            if (search) {
                parameters = JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g, '":"') + '"}')
                historydata.push(parameters['utm_source']);
            }
            localStorage.setItem("ref", JSON.stringify(historydata))

        } else if (document.referrer != '' && localStorage.getItem('ref')) {
            let historydata = []
            let search = location.search.substring(1);
            historydata = JSON.parse(localStorage.getItem("ref"))
            historydata.push(getdomainName(document.referrer))
            if (search) {
                parameters = JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g, '":"') + '"}')
                historydata.push(parameters['utm_source']);
            }
            localStorage.setItem("ref", JSON.stringify(historydata))

        } else if (document.referrer == '' && localStorage.getItem('ref')) {
            let historydata = []
            let search = location.search.substring(1);
            historydata = JSON.parse(localStorage.getItem("ref"))
            historydata.push('direct')
            if (search) {
                parameters = JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g, '":"') + '"}')
                historydata.push(parameters['utm_source']);
            }

            localStorage.setItem("ref", JSON.stringify(historydata))


        }

    }

}


const setup = (data) => {
    let reff = JSON.parse(localStorage.getItem("ref"));

    let filteredArr = reff.filter(function (el) {
        if (el != false && el != null && el != 0 && el != "" && el != undefined && el != NaN) { return el != ''; }

    });

    let store = JSON.parse(localStorage.b24_crm_guest_utm)
    if (reff) {

        for (item of data) {

            try {
                item.innerText = targetemail + filteredArr[filteredArr.length - 1] + targetdomain
                if (item.href) { item.href = 'mailto:' + targetemail + filteredArr[filteredArr.length - 1] + targetdomain }
            } catch (e) {
                continue
            }
        }
        store.list['utm_source'] = filteredArr[filteredArr.length - 1]
    }
    localStorage.b24_crm_guest_utm = JSON.stringify(store)

}



setTimeout(() => {
    detection()

    let cleaner = JSON.parse(localStorage.getItem("ref"));
    if (cleaner.length > 3) {
        cleaner.splice(0, 2)
        localStorage.setItem("ref", JSON.stringify(cleaner))
    }


}, 1000)

