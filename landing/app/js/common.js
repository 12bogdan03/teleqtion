// mobile menu
let toggle = document.querySelector('.nav-toggle');
let menu = document.querySelector('.navbar > ul');
toggle.addEventListener('click', function () {
    this.classList.toggle('opened');
    menu.classList.toggle('open');
});
menu.addEventListener('click', function () {
    this.classList.toggle('opened');
    menu.classList.toggle('open');
});

// sticky header on scroll
window.onscroll = function () {
    let header = document.querySelector('header');
    let scrollpos = window.scrollY;
    if (scrollpos >= header.offsetHeight) {
        header.classList.add('sticky');
    } else {
        header.classList.remove('sticky');
    }
};

// accordion
let acc_btns = document.querySelectorAll('h5 > button');

for (let i = 0; i < acc_btns.length; i++) {
    acc_btns[i].addEventListener("click", function () {
        let current_btn = this;
        this.classList.toggle("collapsed");

        /* Toggle between hiding and showing the active panel */
        let panel = document.querySelector(this.getAttribute('data-target'));
        panel.classList.toggle('show');

        let other_panels = document.querySelectorAll('[id^=collapse]');
        for (let j = 0; j < other_panels.length; j++) {
            if (other_panels[j].getAttribute('id') !== current_btn.getAttribute('data-target').replace('#', '') &&
                other_panels[j].classList.contains('show')) {
                other_panels[j].classList.toggle('show');
            }
            if (acc_btns[j].getAttribute('data-target') !== current_btn.getAttribute('data-target') &&
                !acc_btns[j].classList.contains('collapsed')) {
                acc_btns[j].classList.toggle('collapsed');
            }
        }
    });
}


// scrolling
function makeActive(elem) {
    if (!elem.classList.contains('active')) {
        elem.classList.add('active')
    }
}

function makeOtherInactive(elem, lst) {
    for (let i = 0; i < lst.length; i++) {
        if (lst[i] !== elem) {
            lst[i].classList.remove('active')
        }
    }
}

let anchorLinks = document.querySelectorAll('a[href^="#"]');

for (let item of anchorLinks) {
    item.addEventListener('click', (e) => {
        makeActive(item);
        makeOtherInactive(item, anchorLinks);
        let hashval = item.getAttribute('href');
        let target = document.querySelector(hashval);
        target.scrollIntoView({
            behavior: 'smooth',
            block: 'nearest',
        });
        history.pushState(null, null, hashval);
        e.preventDefault()
    })
}

