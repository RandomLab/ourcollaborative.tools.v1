export function formatDate(dateString, total) {
    if (dateString !== undefined) {

        const date = new Date(dateString)

        const result = new Intl.DateTimeFormat('en-GB', { dateStyle: 'short' }).formatToParts(date)

        const day = result[0]
        const month = result[2]
        const year = result[4]

        if (total) {
            return `${day.value}.${month.value}.${year.value}`
        } else {
            return `${year.value}`
        }
    }
}