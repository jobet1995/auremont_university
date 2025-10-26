from home.models import HomePage, HeroBanner

def run():
    # Get the homepage
    homepage = HomePage.objects.first()
    
    if homepage:
        print(f"Found homepage: {homepage.title}")
        
        # Create a simple hero banner
        hero_banner = HeroBanner.objects.create(
            title="Test Hero Banner"
        )
        
        # Add some content to the hero banner
        hero_banner_content = [
            {
                "type": "hero",
                "value": {
                    "title": "Welcome to Auremont University",
                    "subtitle": "Discover excellence in education",
                    "tagline": "Est. 1952",
                    "background_type": "color",
                    "background_color": "#001F3F"
                }
            }
        ]
        
        # Save the content to the hero banner
        hero_banner.content = hero_banner_content
        hero_banner.save()
        
        # Assign the hero banner to the homepage
        homepage.hero_section = hero_banner
        
        # Add some body content
        body_content = [
            {
                "type": "heading",
                "value": "About Our University"
            },
            {
                "type": "paragraph",
                "value": "<p>Auremont University has been providing quality education for over 70 years. Our commitment to excellence has made us one of the leading institutions in the region.</p>"
            }
        ]
        
        homepage.body = body_content
        homepage.save()
        
        print("Test content added successfully!")
        print(f"Homepage hero section: {homepage.hero_section}")
        print(f"Homepage body: {homepage.body}")
    else:
        print("No homepage found!")

if __name__ == "__main__":
    run()