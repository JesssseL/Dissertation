<template>
    <div 
        :class="`message ${sender === 'ai' ? 'ai-message' : 'user-message'}`"
    >
        <span 
          v-if="sender === 'ai'"
          class="ai-icon material-symbols-outlined"
        > 
            wand_stars
        </span>
        <span
            class="message-text"
        > 
            {{ text }} 
        </span>
    </div>
</template>

<script>
export default {
  name: "AiMessage",
  props: {  
    text: {
      type: String,
      default: ""
    },    
    sender: {
      type: String,
      default: "user"
    },
  }
};
</script>

<style scoped>
.message {
    border-radius: var(--border-radius);
    padding: var(--padding-large);
    width: fit-content;
    max-width: 80%;
    word-break: break-word;
    align-self: flex-end;
    color: var(--main-text);
    padding: var(--padding-large);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-small);
}
.ai-message {
    background-color: white;
    align-self: flex-start;
}
.ai-icon {
    float: left;
    width: 32px;
    height: 32px;
    margin-right: var(--gap);
    color: var(--primary);
    font-size: 32px;
}
.user-message {
    background-color: var(--secondary);
    align-self: flex-end;
}
</style>