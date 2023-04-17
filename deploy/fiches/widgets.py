from django.forms import DateTimeInput
class DateTimePicker(DateTimeInput):
    template_name = 'widgets/datetimepicker.html'
    def get_context(self, name, value, attrs):
        datetimepicker_id = f'datetimepicker_{name}'
        if attrs is None: attrs = dict()
        attrs['data-target'] = f'#{datetimepicker_id}'
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context
    class Media:
        css = {
            "all": (
                "//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
                "//cdnjs.cloudflare.com/ajax/libs/tempusdominus-bootstrap-4/5.39.0/css/tempusdominus-bootstrap-4.min.css",
            )
        }
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.0/moment.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/tempusdominus-bootstrap-4/5.39.0/js/tempusdominus-bootstrap-4.min.js',
        )