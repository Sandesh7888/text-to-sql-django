var ac = {
  // (A) HTML ELEMENTS & PROPERTIES
  // (A1) CLOCK HOUR, MIN, SEC
  chr : null, cmin : null, csec : null,

  // (A2) TIME PICKER HOUR, MIN, SEC, SET, RESET
  thr : null, thm : null, ths : null,
  tset : null, treset : null,

  // (A3) ALARM TIME & SOUND
  alarm : null, sound : null,

  // (B) INITIALIZE ALARM CLOCK
  init : () => {
    // (B1) GET HTML CURRENT TIME - HOUR, MIN, SECONDS
    ac.chr = document.getElementById("chr");
    ac.cmin = document.getElementById("cmin");
    ac.csec = document.getElementById("csec");

    // (B2) CREATE HTML TIME PICKER - HR, MIN, SEC
    ac.thr = ac.createSel(23);
    ac.thm = ac.createSel(59);
    ac.ths = ac.createSel(59);
    document.getElementById("tpick-h").appendChild(ac.thr);
    document.getElementById("tpick-m").appendChild(ac.thm);
    document.getElementById("tpick-s").appendChild(ac.ths);

    // (B3) CREATE HTML TIME PICKER - SET, RESET
    ac.tset = document.getElementById("tset");
    ac.treset = document.getElementById("treset");
    ac.tset.onclick = ac.set;
    ac.treset.onclick = ac.reset;

    // (B4) ALARM SOUND
    ac.sound = new Audio("wake-up-sound.mp3");

    // (B5) START THE CLOCK
    ac.alarm = null;
    setInterval(ac.tick, 1000);
  },

  // (C) SUPPORT FUNCTION - CREATE SELECTOR FOR HR, MIN, SEC
  createSel : (max) => {
    let selector = document.createElement("select"), opt;
    for (let i=0; i<=max; i++) {
      opt = document.createElement("option");
      i = ac.padzero(i);
      opt.value = i;
      opt.innerHTML = i;
      selector.appendChild(opt);
    }
    return selector;
  },

  // (D) SUPPORT FUNCTION - PREPEND HR, MIN, SEC WITH 0 (IF < 10)
  padzero : (num) => {
    if (num < 10) { num = "0" + num; }
    else { num = num.toString(); }
    return num;
  },

  // (E) UPDATE CURRENT TIME
  tick : () => {
    // (E1) CURRENT TIME
    let now = new Date(),
        hr = ac.padzero(now.getHours()),
        min = ac.padzero(now.getMinutes()),
        sec = ac.padzero(now.getSeconds());

    // (E2) UPDATE HTML CLOCK
    ac.chr.innerHTML = hr;
    ac.cmin.innerHTML = min;
    ac.csec.innerHTML = sec;

    // (E3) CHECK AND SOUND ALARM
    if (ac.alarm != null) {
      now = hr + min + sec;
      if (now == ac.alarm && ac.sound.paused) { ac.sound.play(); }
    }
  },

  // (F) SET ALARM
  set : () => {
    ac.alarm = ac.thr.value + ac.thm.value + ac.ths.value;
    ac.thr.disabled = true;
    ac.thm.disabled = true;
    ac.ths.disabled = true;
    ac.tset.disabled = true;
    ac.treset.disabled = false;
  },

  // (G) RESET ALARM
  reset : () => {
    if (!ac.sound.paused) { ac.sound.pause(); }
    ac.alarm = null;
    ac.thr.disabled = false;
    ac.thm.disabled = false;
    ac.ths.disabled = false;
    ac.tset.disabled = false;
    ac.treset.disabled = true;
  }
};

// (H) START CLOCK ON PAGE LOAD
window.addEventListener("load", ac.init);
