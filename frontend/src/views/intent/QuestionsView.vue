<template>
    <div class="questions container">
        <div class="header">
          <h1> Lets find what's right for you </h1>
          <h2> Answer a few quick questions </h2>
        </div>

        <div class="questions_forms">
            <details v-for="question in questions">
                <summary>
                    <div class="question_details">
                        <h3>{{ question.query }}</h3>
                        <p>{{ question.example }}</p>
                    </div>
                    <span
                        v-if="!question.answer.trim().length > 0"
                        class="question_unanswered material-symbols-outlined">
                        arrow_forward_ios
                    </span>
                    <span 
                        v-else
                        class="material-symbols-outlined">
                        check
                    </span>
                </summary>
                <div class="question_answers">
                    Your answer
                    <textarea 
                        v-model="question.answer"
                        placeholder="Type your answer here">
                    </textarea>
                </div>
            </details>
        </div>

        <AppButton 
          text="Next"
          :disabled="!questionsAnswered"
          rightIcon="arrow_forward"
          @click="saveFeatures"
        />
    </div>
</template>

<script>
import AppButton from '@/elements/AppButton.vue'
import SelectableTag from '@/elements/SelectableTag.vue';
import { useSearchStore } from '../../stores/searchStore'
import { useDiscoveryStore } from '../../stores/discoveryStore'

export default {
  name: "QuestionsView",
  components: {
    AppButton,
    SelectableTag
  },
  data() {
    return {
      searchStore: useSearchStore(),
      discoveryStore: useDiscoveryStore(),
      questions: [],
    }
  },
  computed: {
    questionsAnswered() {
      return this.questions.every(question => question.answer.trim().length > 0)
    }
  },
  mounted() {
    this.questions = this.discoveryStore.questions.map(question => ({
      query: question.question,
      example: question.example,
      answer: ''
    }))
  },
  methods: {
    saveFeatures() {
      this.searchStore.addQuestionsAndAnswers(this.questions)
      this.$router.push('/budget')
    }
  },
};
</script>

<style scoped>
.questions {
  display: flex;
  flex-direction: column;
  height: 100%;
  gap: 5px;
}
button {
  margin-top: auto;
  align-self: flex-end;
}
.questions_forms {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.questions_forms details {
    border: 1px solid var(--primary);
    border-radius: var(--border-radius);
    overflow: hidden;
}
.questions_forms details[open] .question_unanswered {
    transform: rotate(90deg);
}
.questions_forms summary {
    background: var(--light);
    display: flex;
    padding: var(--padding-large);
    align-items: center;
}
.questions_forms .question_details {
    display: flex;
    flex-direction: column;
    flex: 1;
}
.questions_forms h3 {
    font-size: 1.5rem;
    font-weight: 600;
    font-family: var(--font-secondary);
    letter-spacing: 0.02em;
}
.questions_forms .question_answers {
    border-top: 1px solid var(--primary);
    display: flex;
    flex-direction: column;
    gap: var(--gap);
    padding: var(--padding-large);
}
</style>