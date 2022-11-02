<template>
  <div class="border">
    <h1>This is Component</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from "@/components/MyComponentItem";

export default {
  name: "MyComponent", // 이름을 지어줘야 다른 곳에서 가져가서 쓸 수 있음

  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: "이건 동적인 데이터!",
    };
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log("용돈 없어!!");
      console.log(childData);
    },
    getDynamicData: function (childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData}입니다.`);
    },
  },
};
</script>

<style>
.border {
  border: solid 1px black;
}
</style>
