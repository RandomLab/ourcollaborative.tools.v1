<script setup>

    import { ref, reactive, computed, onMounted } from 'vue'

    import { marked } from 'marked'

    import { storeToRefs } from 'pinia'
    import { useNotionStore } from '../store/notions'

    const { notions,  loading, error } = storeToRefs(useNotionStore())

    const { fetchNotions } = useNotionStore()

    onMounted(() => {
        fetchNotions()
    })

    const state = ref(true)

    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    function filterByLetter(notions, letter) {
        const filterNotion = notions.filter((item) => {
            return item.title.charAt(0).toLowerCase() === letter
        })
        return filterNotion
    }
    
    function triAlpha(arr) {

        if (state.value) {
            arr.sort((a, b) => {
                    
                if (a < b) {
                    return -1
                }

                if (a > b) {
                    return 1
                }
                return 0

            })
        } else {
            arr.reverse((a, b) => {
                    
                if (a < b) {
                    return -1
                }

                if (a > b) {
                    return 1
                }
                return 0

            })
        }
        return arr
    }

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        <div class="filters">
            <button @click="state = true">ascending</button>
            <button @click="state = false">descending</button>
        </div>

        <div class="notion--container">

            

            <div 
                v-for="(letter, index) in triAlpha(alphabet)"
                :key="index"
            >
                <div 
                    v-if="filterByLetter(notions, letter).length"
                    class="lettrine">
                    {{ letter }}.
                </div>

                <div 
                    v-if="filterByLetter(notions, letter)" 
                    class="notion--list"
                >
                    
                    <div 
                        
                        v-for="notion in filterByLetter(notions, letter)"
                        :key="notion.id"
                        class="notion--item"
                    >
                        <h2><router-link :to="`notion/${notion.slug}`">{{ notion.title }}</router-link></h2>
                        <p v-html="marked.parse(notion.content)"></p>

                    </div>

                </div>

            </div>             
        
        </div>

    </main>
</template>

<style scoped>

.notion--container {
    flex-direction: column;
}
.notion--item {
    width: calc(100%/3);
}
</style>