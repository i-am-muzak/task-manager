<template>
  <div>
    {{ content }}
    <bubble-menu
      :editor="editor"
      :tippy-options="{ duration: 100 }"
      v-if="editor"
      class="bg-white border shadow-lg rounded-[4px] flex"
    >
      <a-tooltip>
        <template #title>Ask to ChatGPT</template>
        <button
          :class="{ 'is-active': editor.isActive('bold') }"
          class="flex items-center p-2 hover:bg-gray-100 text-pink-700 border-r"
        >
          <span class="mr-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="icon icon-tabler icon-tabler-brand-openai"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path
                d="M11.217 19.384a3.501 3.501 0 0 0 6.783 -1.217v-5.167l-6 -3.35"
              ></path>
              <path
                d="M5.214 15.014a3.501 3.501 0 0 0 4.446 5.266l4.34 -2.534v-6.946"
              ></path>
              <path
                d="M6 7.63c-1.391 -.236 -2.787 .395 -3.534 1.689a3.474 3.474 0 0 0 1.271 4.745l4.263 2.514l6 -3.348"
              ></path>
              <path
                d="M12.783 4.616a3.501 3.501 0 0 0 -6.783 1.217v5.067l6 3.45"
              ></path>
              <path
                d="M18.786 8.986a3.501 3.501 0 0 0 -4.446 -5.266l-4.34 2.534v6.946"
              ></path>
              <path
                d="M18 16.302c1.391 .236 2.787 -.395 3.534 -1.689a3.474 3.474 0 0 0 -1.271 -4.745l-4.308 -2.514l-5.955 3.42"
              ></path>
            </svg>
          </span>
          <span class="text-[12px]" style="font-weight: 500"> Ask AI </span>
        </button>
      </a-tooltip>

      <a-tooltip>
        <template #title>Insert URL into selected text</template>
        <button
          :class="{ 'is-active': editor.isActive('bold') }"
          class="flex items-center p-2 hover:bg-gray-100 border-r"
        >
          <span class="mr-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="icon icon-tabler icon-tabler-external-link"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path
                d="M12 6h-6a2 2 0 0 0 -2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-6"
              ></path>
              <path d="M11 13l9 -9"></path>
              <path d="M15 4h5v5"></path>
            </svg>
          </span>
          <span class="text-[12px]" style="font-weight: 500"> Link </span>
        </button>
      </a-tooltip>

      <a-tooltip>
        <template #title>Bold</template>
        <button
          :class="{ 'is-active': editor.isActive('bold') }"
          class="flex items-center p-2 hover:bg-gray-100"
        >
          <span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="icon icon-tabler icon-tabler-bold"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M7 5h6a3.5 3.5 0 0 1 0 7h-6z"></path>
              <path d="M13 12h1a3.5 3.5 0 0 1 0 7h-7v-7"></path>
            </svg>
          </span>
        </button>
      </a-tooltip>

      <a-tooltip>
        <template #title>Italic</template>
        <button
          :class="{ 'is-active': editor.isActive('bold') }"
          class="flex items-center p-2 hover:bg-gray-100"
        >
          <span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="icon icon-tabler icon-tabler-italic"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M11 5l6 0"></path>
              <path d="M7 19l6 0"></path>
              <path d="M14 5l-4 14"></path>
            </svg>
          </span>
        </button>
      </a-tooltip>
      <a-tooltip>
        <template #title>Underline</template>
        <button
          :class="{ 'is-active': editor.isActive('bold') }"
          class="flex items-center p-2 hover:bg-gray-100"
        >
          <span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="icon icon-tabler icon-tabler-underline"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M7 5v5a5 5 0 0 0 10 0v-5"></path>
              <path d="M5 19h14"></path>
            </svg>
          </span>
        </button>
      </a-tooltip>

      <a-tooltip>
        <template #title>Strike</template>
        <button
          :class="{ 'is-active': editor.isActive('bold') }"
          class="flex items-center p-2 hover:bg-gray-100"
        >
          <span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="icon icon-tabler icon-tabler-strikethrough"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M5 12l14 0"></path>
              <path
                d="M16 6.5a4 2 0 0 0 -4 -1.5h-1a3.5 3.5 0 0 0 0 7h2a3.5 3.5 0 0 1 0 7h-1.5a4 2 0 0 1 -4 -1.5"
              ></path>
            </svg>
          </span>
        </button>
      </a-tooltip>

      <a-tooltip>
        <template #title>Insert Code</template>
        <button
          :class="{ 'is-active': editor.isActive('bold') }"
          class="flex items-center p-2 hover:bg-gray-100 border-r"
        >
          <span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="icon icon-tabler icon-tabler-code"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M7 8l-4 4l4 4"></path>
              <path d="M17 8l4 4l-4 4"></path>
              <path d="M14 4l-4 16"></path>
            </svg>
          </span>
        </button>
      </a-tooltip>

      <a-popover
        title="Colors"
        trigger="click"
        placement="rightTop"
        v-model:visible="showColorPicker"
      >
        <template #content>
          <div class="max-h-[230px] overflow-scroll">
            <div v-for="(item, index) in computedColors" :key="index">
              <div
                v-for="(swatch, colorIdx) in item.swatches"
                class="flex items-center p-1 mb-0.5 hover:bg-gray-100 cursor-pointer rounded-[4px]"
                :key="colorIdx"
                @click="setTextColor(swatch.color)"
              >
                <span
                  class="w-[25px] h-[25px] rounded-[4px] mr-2"
                  :style="{ backgroundColor: swatch.color }"
                >
                </span>
                <span class="capitalize text-[12px]">
                  {{ item.paletteName }} - {{ swatch.name }}
                </span>
              </div>
            </div>
          </div>
        </template>
        <a-tooltip>
          <template #title>Pick a color</template>
          <button
            :class="{ 'is-active': editor.isActive('bold') }"
            class="flex items-center p-2 hover:bg-gray-100"
          >
            <span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="icon icon-tabler icon-tabler-palette"
                width="18"
                height="18"
                viewBox="0 0 24 24"
                stroke-width="2"
                stroke="currentColor"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path
                  d="M12 21a9 9 0 0 1 0 -18c4.97 0 9 3.582 9 8c0 1.06 -.474 2.078 -1.318 2.828c-.844 .75 -1.989 1.172 -3.182 1.172h-2.5a2 2 0 0 0 -1 3.75a1.3 1.3 0 0 1 -1 2.25"
                ></path>
                <path d="M8.5 10.5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"></path>
                <path d="M12.5 7.5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"></path>
                <path d="M16.5 10.5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"></path>
              </svg>
            </span>
          </button>
        </a-tooltip>
      </a-popover>
    </bubble-menu>

    <editor-content :editor="editor" />
  </div>
</template>

<script>
import _ from "lodash";

// Tiptap Plugins
import CodeBlockLowlight from "@tiptap/extension-code-block-lowlight";
import Placeholder from "@tiptap/extension-placeholder";
import { Editor, EditorContent, BubbleMenu } from "@tiptap/vue-3";
import { Color } from "@tiptap/extension-color";
import TextStyle from "@tiptap/extension-text-style";
import TaskItem from "@tiptap/extension-task-item";
import TaskList from "@tiptap/extension-task-list";

// Highlight JS
import { lowlight } from "lowlight";
import "@/assets/hljs-one-dark.css";

// Tiptap Configuration
import StarterKit from "@tiptap/starter-kit";
import Commands from "../plugins/tiptap/commands";
import suggestion from "../plugins/tiptap/suggestion";

// Color Palette from Tailwind
import { colorPalette } from "@/plugins/tailwind/palette";

export default {
  components: {
    EditorContent,
    BubbleMenu,
  },

  data() {
    return {
      editor: null,
      showColorPicker: false,
      content: "",
    };
  },

  methods: {
    setTextColor(color) {
      if (this.editor) {
        this.editor.chain().focus().setColor(color).run();
        this.showColorPicker = false;
      }
    },
    updateContent: _.debounce(function (content) {
      this.content = content;
    }, 1000),
  },

  mounted() {
    this.editor = new Editor({
      extensions: [
        StarterKit,
        Color,
        TextStyle,
        Placeholder.configure({
          placeholder: "Press '/' for commands...",
        }),
        CodeBlockLowlight.configure({ lowlight }),
        Commands.configure({
          suggestion,
        }),
        TaskList,
        TaskItem.configure({
          nested: true,
        }),
      ],
      content: ``,
      onUpdate: () => {
        this.updateContent(this.editor.getHTML());
      },
    });
  },

  beforeUnmount() {
    this.editor.destroy();
  },

  computed: {
    computedColors() {
      return colorPalette;
    },
  },
};
</script>

<style lang="less" scoped>
::v-deep(.tippy-box) {
  max-width: none !important;
}

::v-deep(.ProseMirror) {
  border: none;
  outline: none;
  color: rgb(55, 53, 47);
  font-family: "Inter", sans-serif;
  font-size: 14px;

  p.is-empty::before {
    content: attr(data-placeholder);
    float: left;
    color: #adb5bd;
    pointer-events: none;
    height: 0;
    font-size: 14px;
  }

  > * + * {
    margin-top: 0.75em;
  }

  h1 {
    font-size: 1.5rem;
    font-weight: 600;
  }

  h2 {
    font-size: 1.25rem;
    font-weight: 600;
  }

  h3 {
    font-size: 1.15rem;
    font-weight: 600;
  }

  ul {
    list-style: disc !important;
    padding-left: 24px;
  }

  ul[data-type="taskList"] {
    padding-left: 0 !important;
    li {
      display: flex !important;

      > label {
        flex: 0 0 auto;
        margin-right: 0.5rem;
        user-select: none;
      }

      > div {
        flex: 1 1 auto;
        p {
          margin: 0;
        }
      }
    }
  }

  ol {
    list-style: decimal !important;
    padding-left: 24px;
  }

  code {
    display: block;
    overflow-x: auto;
    padding: 0.5em;
    background: #e5e6e7;
    border-radius: 4px;
    font-size: 12px;
  }

  pre {
    code {
      display: block;
      overflow-x: auto;
      padding: 0.5em;
      color: #abb2bf;
      background: #282c34;
      border-radius: 4px;
      font-size: 12px;
    }
  }
}

// Command Menu styling
::v-deep(.mention) {
  border: 1px solid #000;
  border-radius: 0.4rem;
  padding: 0.1rem 0.3rem;
  box-decoration-break: clone;
}

// Checkbox (TodoList)
::v-deep(ul[data-type="taskList"]) {
  label {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  input[type="checkbox"] {
    --active-inner: #fff;
    --focus: 2px rgba(59, 60, 65, 0.3);
    --border: #6c6e70;
    --border-hover: #414244;
    --background: #fff;
    --disabled: #f6f8ff;
    --disabled-inner: #e1e6f9;
    -webkit-appearance: none;
    -moz-appearance: none;
    height: 16px;
    outline: none;
    display: inline-block;
    vertical-align: top;
    position: relative;
    margin: 0;
    cursor: pointer;
    border: 1px solid var(--bc, var(--border));
    background: var(--b, var(--background));
    transition: background 0.3s, border-color 0.3s, box-shadow 0.2s;
  }
  input[type="checkbox"]:after {
    content: "";
    display: block;
    left: 0;
    top: 0;
    position: absolute;
    transition: transform var(--d-t, 0.3s) var(--d-t-e, ease),
      opacity var(--d-o, 0.2s);
  }
  input[type="checkbox"]:checked {
    --d-o: 0.3s;
    --d-t: 0.6s;
    --d-t-e: cubic-bezier(0.2, 0.85, 0.32, 1.2);
  }
  input[type="checkbox"]:disabled {
    --b: var(--disabled);
    cursor: not-allowed;
    opacity: 0.9;
  }
  input[type="checkbox"]:disabled:checked {
    --b: var(--disabled-inner);
    --bc: var(--border);
  }
  input[type="checkbox"]:disabled + label {
    cursor: not-allowed;
  }
  input[type="checkbox"]:hover:not(:checked):not(:disabled) {
    --bc: var(--border-hover);
  }
  input[type="checkbox"]:focus {
    box-shadow: 0 0 0 var(--focus);
  }
  input[type="checkbox"]:not(.switch) {
    width: 16px;
  }
  input[type="checkbox"]:not(.switch):after {
    opacity: var(--o, 0);
  }
  input[type="checkbox"]:not(.switch):checked {
    --o: 1;
  }
  input[type="checkbox"] + label {
    display: inline-block;
    vertical-align: middle;
    cursor: pointer;
    margin-left: 4px;
  }

  input[type="checkbox"]:not(.switch) {
    border-radius: 2px;
  }
  input[type="checkbox"]:not(.switch):after {
    width: 5px;
    height: 9px;
    border: 2px solid var(--border);
    border-top: 0;
    border-left: 0;
    left: 5px;
    top: 1.5px;
    transform: rotate(var(--r, 20deg));
  }
  input[type="checkbox"]:not(.switch):checked {
    --r: 43deg;
  }

  li[data-checked="true"] {
    p {
      color: rgba(55, 53, 47, 0.65);
      text-decoration: line-through;
    }
  }
}
</style>
