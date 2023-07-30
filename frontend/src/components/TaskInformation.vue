<template>
  <div>
    <div>
      <a-drawer
        v-model:visible="isVisible"
        placement="right"
        @close="onDrawerClose"
        :mask="true"
        :headerStyle="{ display: 'none' }"
        :width="800"
      >
        <div class="title-input mb-5">
          <a-textarea
            v-model:value="task_title"
            placeholder="Untitled"
            auto-size
            :bordered="false"
            @pressEnter="preventEnterEvent"
            @change="handleTitleChange"
          />
        </div>
        <div class="flex flex-col">
          <div class="flex items-center">
            <div class="flex items-center task-property-text">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-users"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  stroke-width="1.25"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M9 7m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0"></path>
                  <path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                  <path d="M21 21v-2a4 4 0 0 0 -3 -3.85"></path>
                </svg>
              </span>
              <span class="ml-2"> Assign </span>
            </div>
            <div class="w-full">
              <a-select
                placeholder="Assign this task to selected people..."
                class="w-full"
                v-model:value="assigned"
                mode="multiple"
              >
                <a-select-option
                  :value="user.id"
                  v-for="user in userData"
                  :key="user.id"
                  >{{ user.name }}</a-select-option
                >
              </a-select>
            </div>
          </div>

          <div class="flex items-center mt-2">
            <div class="flex items-center task-property-text">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-status-change"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  stroke-width="1.25"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M6 18m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"></path>
                  <path d="M18 18m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"></path>
                  <path d="M6 12v-2a6 6 0 1 1 12 0v2"></path>
                  <path d="M15 9l3 3l3 -3"></path>
                </svg>
              </span>
              <span class="ml-2"> Status </span>
            </div>
            <div class="w-full">
              <a-select
                placeholder="Empty"
                class="w-full"
                v-model:value="assigned"
              >
                <a-select-option
                  :value="user.id"
                  v-for="user in userData"
                  :key="user.id"
                  >{{ user.name }}</a-select-option
                >
              </a-select>
            </div>
          </div>

          <div class="flex items-center mt-2">
            <div class="flex items-center task-property-text">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-mobiledata"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  stroke-width="1.25"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M16 12v-8"></path>
                  <path d="M8 20v-8"></path>
                  <path d="M13 7l3 -3l3 3"></path>
                  <path d="M5 17l3 3l3 -3"></path>
                </svg>
              </span>
              <span class="ml-2"> Priority </span>
            </div>
            <div class="w-full">
              <a-select
                placeholder="Empty"
                class="w-full"
                v-model:value="assigned"
              >
                <a-select-option
                  :value="user.id"
                  v-for="user in userData"
                  :key="user.id"
                  >{{ user.name }}</a-select-option
                >
              </a-select>
            </div>
          </div>

          <div class="flex items-center mt-2">
            <div class="flex items-center task-property-text">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-clock-hour-3"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  stroke-width="1.25"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"></path>
                  <path d="M12 12h3.5"></path>
                  <path d="M12 7v5"></path></svg
              ></span>
              <span class="ml-2"> Date Created </span>
            </div>
            <div class="w-full">
              <a-select
                placeholder="Empty"
                class="w-full"
                v-model:value="assigned"
              >
                <a-select-option
                  :value="user.id"
                  v-for="user in userData"
                  :key="user.id"
                  >{{ user.name }}</a-select-option
                >
              </a-select>
            </div>
          </div>

          <div class="flex items-center mt-2">
            <div class="flex items-center task-property-text">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-calendar"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  stroke-width="1.25"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path
                    d="M4 7a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12z"
                  ></path>
                  <path d="M16 3v4"></path>
                  <path d="M8 3v4"></path>
                  <path d="M4 11h16"></path>
                  <path d="M11 15h1"></path>
                  <path d="M12 15v3"></path></svg
              ></span>
              <span class="ml-2"> Date Started </span>
            </div>
            <div class="w-full">
              <a-select
                placeholder="Empty"
                class="w-full"
                v-model:value="assigned"
              >
                <a-select-option
                  :value="user.id"
                  v-for="user in userData"
                  :key="user.id"
                  >{{ user.name }}</a-select-option
                >
              </a-select>
            </div>
          </div>

          <div class="flex items-center mt-2">
            <div class="flex items-center task-property-text">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-hourglass-empty"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  stroke-width="1.25"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path
                    d="M6 20v-2a6 6 0 1 1 12 0v2a1 1 0 0 1 -1 1h-10a1 1 0 0 1 -1 -1z"
                  ></path>
                  <path
                    d="M6 4v2a6 6 0 1 0 12 0v-2a1 1 0 0 0 -1 -1h-10a1 1 0 0 0 -1 1z"
                  ></path></svg
              ></span>
              <span class="ml-2"> Estimated Effort </span>
            </div>
            <div class="w-full">
              <a-select
                placeholder="Empty"
                class="w-full"
                v-model:value="assigned"
              >
                <a-select-option
                  :value="user.id"
                  v-for="user in userData"
                  :key="user.id"
                  >{{ user.name }}</a-select-option
                >
              </a-select>
            </div>
          </div>
        </div>
        <a-divider />
        <div>
          <InformationEditor />
        </div>
      </a-drawer>
    </div>
  </div>
</template>

<script>
import InformationEditor from "@/components/InformationEditor.vue";

export default {
  components: {
    InformationEditor,
  },
  props: {
    visible: {
      type: Boolean,
      default: false,
    },
    data: {
      type: Object,
      default: () => {
        return {};
      },
    },
  },
  data() {
    return {
      isVisible: false,
      task_title: "",
      assigned: [],
      userData: [
        {
          id: (Math.random() + 1).toString(36).substring(7),
          name: "Hasan",
        },
        {
          id: (Math.random() + 1).toString(36).substring(7),
          name: "Ali",
        },
        {
          id: (Math.random() + 1).toString(36).substring(7),
          name: "Lorem",
        },
      ],
    };
  },
  methods: {
    onDrawerClose() {
      this.$emit("closed");
    },
    preventEnterEvent(event) {
      event.preventDefault();
    },
    handleTitleChange() {
      this.$emit("titleChanged", this.task_title);
    },
  },
  watch: {
    visible: {
      handler(newValue) {
        this.isVisible = newValue;
      },
      immediate: true,
    },
    data: {
      handler(newValue) {
        this.task_title = newValue.title;
      },
    },
  },
};
</script>

<style lang="less" scoped>
::v-deep(.ant-input) {
  font-size: 24px !important;
  font-weight: 700  !important;
  border-radius: 5px;
  &:hover {
    background-color: rgb(237, 237, 237);
  }
}

.task-property-text {
  min-width: 170px;
}

:deep(.ant-select-selection-item-remove) {
  line-height: normal !important;
}
</style>
