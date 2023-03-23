<script setup>

    import { storeToRefs } from 'pinia'
    import { useNotionStore } from '../store/notions'

    import NotionProjects from '../components/notion/NotionProjects.vue'

    const { notions, loading, error } = storeToRefs(useNotionStore())

    const { fetchNotions } = useNotionStore()

    fetchNotions()

    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    function filterByLetter(notions, letter) {
        const filterNotion = notions.filter((item) => {
            return item.title.charAt(0).toLowerCase() === letter
        })
        return filterNotion
    }

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        <div 
            v-for="(letter, index) in alphabet"
            :key="index"
        >
            <div 
                v-if="filterByLetter(notions, letter).length"
                class="lettrine">
                {{ letter }}.
            </div>

            <div 
                v-if="filterByLetter(notions, letter)" 
                class="notion"
            >
                
                <div 
                    
                    v-for="notion in filterByLetter(notions, letter)"
                    :key="notion.id"
                    class="notion--item"
                >
                    <h2><router-link :to="`notion/${notion.slug}`">{{ notion.title }}</router-link></h2>
                    <p>{{ notion.content }}</p>

                </div>

            </div>

        </div>        

    </main>
</template>