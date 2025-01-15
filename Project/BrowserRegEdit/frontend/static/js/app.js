$(document).ready(function()
{
    // Handle the form submission.
    $('#create-registry-form').on('submit', function(e)
    {
        e.preventDefault();
        
        // Get the values from the form.
        const key = $('#key').val();
        const value = $('#value').val();
        const type = $('#type').val();
        const permissions = $('#permissions').val();
        const lastModified = $('#last_modified').val();

        // Send the data to the Back-End.
        $.ajax(
            {
                url: '/create_registry',
                method: 'POST',
                data: {
                    key: key,
                    value: value,
                    type: type,
                    permissions: permissions,
                    last_modified: lastModified
            },

            success: function(updatedRegistry)
            {
                $('#registry-list').empty();
                for (let key in updatedRegistry) {
                    $('#registry-list').append('<li>' + key + ': ' + updatedRegistry[key] + '</li>');
                }
                
                $('#key').val('');
                $('#value').val('');
                $('#permissions').val('');
                $('#last_modified').val('');
            },

            error: function(error)
            {
                console.error('Error creating registry:', error);
            }
        });
    });
});