"""
GitLab Agent Configuration Search
"""
import os
import gitlab

def search_gitlab_agents():
    # Initialize GitLab connection
    gl = gitlab.Gitlab('https://gitlab.com', private_token=os.environ['GITLAB_TOKEN'])
    
    # Known project IDs
    projects = {
        'agent-configurations-secure': 65967939,
        'core-agency-confidential': 65967876,
        'dr-memoria-learning-core': 65967838
    }
    
    # Search for agent configurations
    agents_to_find = [
        'dr.grant', 'dr.lucy', 'mr.roark', 'dr.maria', 
        'dr.memoria', 'professor.lee', 'dr.sabina', 
        'claude.ai', 'dr.burby', 'dr.cypriot', 'dr.match'
    ]
    
    found_configs = {}
    
    for name, project_id in projects.items():
        project = gl.projects.get(project_id)
        try:
            items = project.search('all', ' '.join(agents_to_find))
            if items:
                found_configs[name] = items
        except Exception as e:
            print(f"Error searching {name}: {str(e)}")
            
    return found_configs