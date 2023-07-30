<template>
  <div>
    <draggable
      :list="taskData"
      :group="{ name: 'tasks' }"
      @start="drag = true"
      @end="drag = false"
      :emptyInsertThreshold="50"
    >
      <template #item="{ element }">
        <div @click="showTaskPage(element)" v-click-away="handleClickAway">
          <div
            class="task-section rounded-[4px] mb-2 cursor-pointer select-none hover:bg-gray-50 transition duration-200 p-3"
            :class="!element.editModeEnabled ? '' : 'edit-mode-enabled'"
          >
            <div
              @click.stop="
                handleTagPopoverTrigger(element.editModeEnabled, element)
              "
              :id="`task_section_${element.group_id}#${element.id}`"
            >
              <div class="flex justify-between">
                <div class="flex w-full items-center">
                  <div v-if="!element.editModeEnabled" class="p-1">
                    {{ element.title ? element.title : "Untitled" }}
                  </div>

                  <div v-else class="w-full">
                    <div>
                      <input
                        class="outline-none bg-inherit w-full hover:bg-gray-200 p-1 rounded transition duration-200"
                        type="text"
                        placeholder="Untitled..."
                        v-model="element.title"
                        @click.stop
                        :tabindex="element.id"
                        :id="`_task_input_${element.id}`"
                        :ref="`task_input_${element.id}`"
                        @keypress.enter="handleClickAway"
                      />
                    </div>
                  </div>
                </div>
                <div
                  class="task-settings-section flex text-gray-400 bg-white rounded"
                >
                  <a-tooltip>
                    <template #title>
                      <span class="text-[12px]"> Edit </span>
                    </template>
                    <span
                      class="task-icon hover:text-gray-700 hover:bg-gray-200 border-r rounded-tl rounded-bl p-[5px]"
                      @click.stop="enableEditMode(element)"
                    >
                      <span class="flex items-center justify-center">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          class="icon icon-tabler icon-tabler-pencil"
                          width="16"
                          height="16"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          fill="none"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                        >
                          <path
                            stroke="none"
                            d="M0 0h24v24H0z"
                            fill="none"
                          ></path>
                          <path
                            d="M4 20h4l10.5 -10.5a2.828 2.828 0 1 0 -4 -4l-10.5 10.5v4"
                          ></path>
                          <path d="M13.5 6.5l4 4"></path>
                        </svg>
                      </span>
                    </span>
                  </a-tooltip>

                  <a-tooltip>
                    <template #title>
                      <span class="text-[12px]">
                        Delete, duplicate, edit...
                      </span>
                    </template>
                    <span
                      class="task-icon hover:text-gray-700 hover:bg-gray-200 rounded-tr rounded-br p-[5px]"
                    >
                      <span class="flex items-center justify-center">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          class="icon icon-tabler icon-tabler-dots"
                          width="16"
                          height="16"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          fill="none"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                        >
                          <path
                            stroke="none"
                            d="M0 0h24v24H0z"
                            fill="none"
                          ></path>
                          <path
                            d="M5 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                          ></path>
                          <path
                            d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                          ></path>
                          <path
                            d="M19 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                          ></path>
                        </svg>
                      </span>
                    </span>
                  </a-tooltip>
                </div>
              </div>

              <div v-if="element.tags.length" class="flex items-center">
                <a-tooltip placement="left">
                  <template #title>
                    <span class="text-[12px]">Project</span>
                  </template>

                  <div
                    class="my-1 pb-1 px-1 transition duration-200 rounded-[3px] hover:bg-gray-200"
                  >
                    <div
                      class="inline-block text-[10px] px-1 py-0.5 rounded-[3px] leading-[19px] mt-1"
                      :class="
                        getComputedGroupColor(
                          tag.color,
                          index,
                          element.tags.length
                        )
                      "
                      v-for="(tag, index) in element.tags"
                      :key="index"
                    >
                      {{ tag.title }}
                    </div>
                  </div>
                </a-tooltip>
              </div>

              <a-popover
                trigger="click"
                placement="bottomLeft"
                overlayClassName="custom-tab-popover w-[380px]"
                :align="{
                  offset: [-15, -30],
                }"
                :getPopupContainer="
                  (triggerNode) => getParentElement(triggerNode, element)
                "
              >
                <template #title>
                  <div
                    class="p-2 bg-[#f2f1ee99] flex items-center flex-wrap gap-1"
                  >
                    <div
                      class="flex items-center px-1.5 py-1 cursor-pointer bg-indigo-100 text-indigo-900 font-semibold text-[11px] rounded-[3px]"
                      v-for="(tag, index) in selectedProjects"
                      :key="index"
                    >
                      <span class="mr-2"> {{ tag }} </span>
                      <span @click="deleteTag(tag, index)">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          class="icon icon-tabler icon-tabler-x"
                          width="12"
                          height="12"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          fill="none"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                        >
                          <path
                            stroke="none"
                            d="M0 0h24v24H0z"
                            fill="none"
                          ></path>
                          <path d="M18 6l-12 12"></path>
                          <path d="M6 6l12 12"></path>
                        </svg>
                      </span>
                    </div>
                    <div class="flex items-center grow">
                      <a-input
                        :bordered="false"
                        class="w-full"
                        style="margin: 0; padding: 0"
                        placeholder="Search or create a project..."
                        v-model:value="tagKeyword"
                        @keypress.enter="inputPressEnter"
                      />
                    </div>
                  </div>
                </template>
                <template #content>
                  <div>
                    <div class="p-1 max-h-[200px] overflow-scroll">
                      <h1
                        class="text-[#37352fa6] font-semibold text-[11px] px-2 py-1"
                      >
                        Select an option or create one
                      </h1>
                      <div
                        class="flex items-center rounded-[3px] hover:bg-gray-100 cursor-pointer px-1 py-2 mt-1"
                        v-for="project in filteredProjects"
                        @click="setProject(project)"
                        :class="
                          selectedProjects.includes(project)
                            ? 'bg-gray-100'
                            : ''
                        "
                      >
                        <span class="mr-2 text-gray-400">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="icon icon-tabler icon-tabler-grip-vertical"
                            width="16"
                            height="16"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            fill="none"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                          >
                            <path
                              stroke="none"
                              d="M0 0h24v24H0z"
                              fill="none"
                            ></path>
                            <path
                              d="M9 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                            ></path>
                            <path
                              d="M9 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                            ></path>
                            <path
                              d="M9 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                            ></path>
                            <path
                              d="M15 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                            ></path>
                            <path
                              d="M15 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                            ></path>
                            <path
                              d="M15 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                            ></path>
                          </svg>
                        </span>
                        <span
                          class="inline-block px-1 py-0.5 font-semibold bg-rose-50 text-rose-800 rounded-[3px] text-[11px]"
                          >{{ project }}</span
                        >
                      </div>
                      <div
                        v-if="
                          !this.filteredProjects.filter(
                            (x) => x.toLowerCase() === tagKeyword.toLowerCase()
                          ).length &&
                          !this.selectedProjects.filter(
                            (x) => x.toLowerCase() === tagKeyword.toLowerCase()
                          ).length
                        "
                      >
                        <div
                          v-if="tagKeyword.trim()"
                          class="w-full flex items-center px-2 py-1 bg-gray-100 rounded-[3px] cursor-pointer active:bg-gray-200"
                        >
                          <span class="mr-2">Create:</span>
                          <span
                            class="bg-gray-300 text-gray-900 px-2 py-0.5 rounded-[3px] text-[12px]"
                            >{{ tagKeyword.trim() }}</span
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </template>
                <div
                  v-show="!element.tags.length && element.editModeEnabled"
                  class="flex items-center text-gray-500 p-1 hover:bg-gray-200 rounded-[3px] mt-1 transition duration-200"
                  @click.stop
                >
                  <span class="mr-1">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="icon icon-tabler icon-tabler-list"
                      width="16"
                      height="16"
                      viewBox="0 0 24 24"
                      stroke-width="1.5"
                      stroke="currentColor"
                      fill="none"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    >
                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                      <path d="M9 6l11 0"></path>
                      <path d="M9 12l11 0"></path>
                      <path d="M9 18l11 0"></path>
                      <path d="M5 6l0 .01"></path>
                      <path d="M5 12l0 .01"></path>
                      <path d="M5 18l0 .01"></path>
                    </svg>
                  </span>
                  <span class="text-[11px]"> Add Project </span>
                </div>
              </a-popover>
            </div>
          </div>
        </div>
      </template>
    </draggable>
    <div
      class="flex items-center hover:bg-gray-100 text-gray-400 rounded-[3px] p-2 cursor-pointer hover:text-gray-700 select-none"
      id="_addItemButton"
      @click="insertTask"
    >
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="icon icon-tabler icon-tabler-plus"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          stroke-width="1.75"
          stroke="currentColor"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
          <path d="M12 5l0 14"></path>
          <path d="M5 12l14 0"></path></svg
      ></span>
      <span class="pl-2"> New </span>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";

export default {
  components: {
    draggable,
  },
  props: {
    tasks: {
      type: Array,
      default: [],
    },
  },
  data() {
    return {
      drag: false,
      taskData: [],
      allProjects: ["Backend", "Frontend", "Github", "Slack", "Google"],
      filteredProjects: ["Backend", "Frontend", "Github", "Slack", "Google"],
      tagKeyword: "",
      selectedProjects: [],
    };
  },
  methods: {
    deleteTag(tag, index) {
      this.selectedProjects.splice(index, 1);
      this.filteredProjects.push(tag);
    },
    inputPressEnter() {
      if (!this.tagKeyword.trim()) return;
      for (var i = 0; i < this.filteredProjects.length; i++) {
        const project = this.filteredProjects[i];
        if (project.toLowerCase() === this.tagKeyword.trim().toLowerCase()) {
          // It means there is a match. So we can select the first index here...
          this.selectedProjects.push(project);
          this.tagKeyword = "";
          return;
        }
      }

      if (this.selectedProjects.includes(this.tagKeyword.trim())) {
        // Nothing to do here.
        return;
      }

      // If selected projects don't include the input, we need to add it.
      this.selectedProjects.push(this.tagKeyword.trim());
      this.allProjects.push(this.tagKeyword.trim());
      this.tagKeyword = "";
    },
    setProject(project) {
      const index = this.selectedProjects.findIndex((x) => x === project);
      if (index === -1) {
        this.selectedProjects.push(project);
        this.tagKeyword = "";
        this.filteredProjects = this.filteredProjects.filter(
          (x) => x !== project
        );
      } else {
        // Project already added. So we can delete it.
        this.selectedProjects.splice(index, 1);
        this.tagKeyword = "";
      }
    },
    getComputedGroupColor(color, index, totalLength) {
      if (color) {
        const computedColor = color.toLowerCase();
        const isLastItem = index + 1 === totalLength ? true : false;
        if (computedColor === `rose`)
          return `bg-rose-100 text-rose-700 ${!isLastItem ? "mr-1" : ""}`;
        if (computedColor === `orange`)
          return `bg-orange-100 text-orange-700 ${!isLastItem ? "mr-1" : ""}`;
        if (computedColor === `lime`)
          return `bg-lime-100 text-lime-700 ${!isLastItem ? "mr-1" : ""}`;
        if (computedColor === `indigo`)
          return `bg-indigo-100 text-indigo-700 ${!isLastItem ? "mr-1" : ""}`;
        if (computedColor === `sky`)
          return `bg-sky-100 text-sky-700 ${!isLastItem ? "mr-1" : ""}`;
        if (computedColor === `blue`)
          return `bg-blue-100 text-blue-700 ${!isLastItem ? "mr-1" : ""}`;
        if (computedColor === `yellow`)
          return `bg-yellow-100 text-yellow-700 ${!isLastItem ? "mr-1" : ""}`;
      }
      return "";
    },
    showTaskPage(task) {
      this.$emit("onTaskClicked", task);
    },
    insertTask() {
      this.$emit("insertTask");
    },
    handleClickAway($event) {
      this.$emit("outsideClicked");
    },
    enableEditMode(element) {
      const index = this.taskData.findIndex((x) => x.id == element.id);
      if (index === -1) return;
      else {
        this.$emit("outsideClicked");
        this.taskData[index].editModeEnabled = true;
      }
    },
    getParentElement($event, element) {
      return document.getElementById(
        `task_section_${element.group_id}#${element.id}`
      );
    },
    handleTagPopoverTrigger(editModeEnabled, element) {
      if (editModeEnabled) {
        return;
      }
      this.showTaskPage(element);
    },
  },
  computed: {
    dragOptions() {
      return {
        animation: 200,
        group: "description",
        disabled: false,
      };
    },
  },
  watch: {
    tasks: {
      handler(newValue) {
        this.taskData = newValue;
      },
      deep: true,
      immediate: true,
    },
    tagKeyword(newValue) {
      this.filteredProjects = this.allProjects;
      const regex = new RegExp(newValue, "gmi");
      this.filteredProjects = this.filteredProjects
        .filter((x) => regex.test(x))
        .filter((x) => !this.selectedProjects.includes(x));
    },
  },
};
</script>

<style lang="less" scoped>
::v-deep(.custom-tab-popover) {
  .ant-popover-arrow {
    display: none;
  }
}
.edit-mode-enabled {
  box-shadow: rgba(33, 123, 179, 0.3) 0px 0px 0px 1.5px,
    rgba(33, 123, 179, 0.3) 0px 2px 4px !important;
}
.task-section {
  color: rgb(55, 53, 47);
  font-weight: 600;
  box-shadow: rgba(15, 15, 15, 0.1) 0px 0px 0px 1px,
    rgba(15, 15, 15, 0.1) 0px 2px 4px;
  position: relative;

  .task-settings-section {
    opacity: 0;
    position: absolute;
    right: 8px;
    top: 13px;
    box-shadow: rgba(15, 15, 15, 0.15) 0px 0px 0px 1px,
      rgba(15, 15, 15, 0.3) 0px 2px 7px;
    transition: 0.2s ease-in-out;
  }
  &:hover {
    .task-settings-section {
      opacity: 100;
    }
  }
}

.item-dropzone-area {
  height: 2rem;
  background: #000;
}
</style>
