<script setup>

    import { reactive, ref } from 'vue'

    import { storeToRefs } from 'pinia'
    import { useSearchStore } from '../store/search'

    import Results from '../components/Results.vue'

    const { results, loading, error } = storeToRefs(useSearchStore())

    const { fetchSearch, mergeData } = useSearchStore()

    const search = reactive({
        word: '',
    })

    function launchSearch() {
        fetchSearch(search.word)
        mergeData
        search.word = ''
    }

</script>

<template>
    <main>
        
        <div class="search-index">
            <h2>Search through all</h2>
            <input 
                type="text"
                placeholder="keyword"
                v-model="search.word"
                @keyup.enter="launchSearch"
            >
        </div>

        <div class="search-index-mobile">
            <input 
                type="text"
                placeholder="Search through all"
                v-model="search.word"
            >
            <button @click="launchSearch">go</button>
        </div>

        <div class="loading" v-if="loading">loading</div>
        <div class="error" v-if="error">{{ error.message }}</div>

        <!-- notions -->

        <div 
            v-if="results.length > 0" 
            class="search-results"
        >

            <div
                v-for="result in results"
                :key="result.id"
            >
                <results :result="result"></results>

            </div>

        </div>

        


        <div v-else class="no-result">no results</div>

    </main>
   

</template>