<template>
  <div>
    <h1>Component Item</h1>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭!</button>
    <input type="text" v-model="childInputData" @keyup.enter="childInput" />
  </div>
</template>

<script>
export default {
  name: "MyComponentItem",
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  methods: {
    childToParent: function () {
      this.$emit("child-to-parent", "나는 자식이 보낸 데이터다"); // $가 붙은 이유는 객체의 기본 속성값, 버튼이 눌렸을 때 아우성
      // 두번째 인자부터는 데이터
    },
    childInput: function () {
      this.$emit("child-input", this.childInputData);
    },
  },
  data: function () {
    return {
      childInputData: null,
    };
  },
};
</script>

<style></style>
