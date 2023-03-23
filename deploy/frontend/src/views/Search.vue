<script setup>

    import { reactive } from 'vue'

    import { storeToRefs } from 'pinia'
    import { useSearchStore } from '../store/search'

    const { results, loading, error } = storeToRefs(useSearchStore())

    const { fetchSearch } = useSearchStore()

    const search = reactive({
        word: '',
    })

</script>

<template>
    <main>
        <input 
            type="text"
            placeholder="search"
            v-model="search.word"
            @keyup.enter="fetchSearch(search.word)"
        >

        <div v-if="loading">loading</div>
        <div v-if="error">{{  error.message }}</div>
        <div v-if="results" class="index">
        <li 
            v-for="result in results"
            :key="result.id"
        >
            <RouterLink :to="`/project/${result.slug}`">{{ result.title }}</RouterLink>
        </li>
    </div>

    </main>
   

</template>