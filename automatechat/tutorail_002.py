from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=900)
    
    context = browser.new_context(
        record_video_dir="videostutorial/",
    record_video_size={"width": 640, "height": 480}
    )
    
    page = context.new_page()
    page.goto("https://playwright.dev/")
    # page.screenshot(path="example.png")
    
    #page.wait_for_timeout(1000)
    
    # page.pause()
    
    #page.screenshot(path="example002.png")
    
    browser.close()