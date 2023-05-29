use yew::prelude::*;

mod components;
use crate::components::{AboutPage, Footer, Header};

#[function_component]
fn App() -> Html {

    html! {
        <div className="site">
            <Header />
            <main className="Site-content">
            <AboutPage />
            </main>
            <Footer />
        </div>
    }
}

fn main() {
    let sensor_list = vec![
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "ambient_humidity",
        "ambient_temp",
        "ambient_pressure",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
    ];
    yew::Renderer::<App>::new().render();
}
