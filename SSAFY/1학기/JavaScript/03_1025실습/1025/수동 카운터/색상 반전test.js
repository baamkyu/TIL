const obj = {
  logThis: function () {
    console.log(this); // 여기서의 this : obj자체
  },
  setTime: function () {
    setTimeout(this.logThis, 2000); // window로 날아감
  },
  addEvent: function () {
    body.addEventListener("click", this.logThis); //
  },
};

obj.logThis();
