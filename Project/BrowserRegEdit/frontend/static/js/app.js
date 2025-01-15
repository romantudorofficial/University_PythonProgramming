$(document).ready(function() {
    // Handle form submission
    $('#create-registry-form').on('submit', function(e) {
        e.preventDefault();
        
        // Get values from the form
        const key = $('#key').val();
        const value = $('#value').val();
        const type = $('#type').val();
        const permissions = $('#permissions').val();
        const lastModified = $('#last_modified').val();

        // Send the data to the backend
        $.ajax({
            url: '/create_registry',
            method: 'POST',
            data: {
                key: key,
                value: value,
                type: type,
                permissions: permissions,
                last_modified: lastModified
            },
            success: function(updatedRegistry) {
                // Update the UI with the new registry data
                $('#registry-list').empty(); // Clear the existing list
                for (let key in updatedRegistry) {
                    $('#registry-list').append('<li>' + key + ': ' + updatedRegistry[key] + '</li>');
                }
                
                // Clear the input fields after successful creation
                $('#key').val('');
                $('#value').val('');
                $('#permissions').val('');
                $('#last_modified').val('');
            },
            error: function(error) {
                console.error('Error creating registry:', error);
            }
        });
    });
});
