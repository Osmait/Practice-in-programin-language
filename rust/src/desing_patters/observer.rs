use std::collections::HashMap;

#[derive(Default)]
pub struct Editor {
    publisher: Publisher,
    file_path: String,
}

impl Editor {
    pub fn events(&mut self) -> &mut Publisher {
        &mut self.publisher
    }

    pub fn load(&mut self, path: String) {
        self.file_path = path.clone();
        self.publisher.notify(Event::Load, path);
    }

    pub fn save(&self) {
        self.publisher.notify(Event::Save, self.file_path.clone());
    }
}

/// An event type.
#[derive(PartialEq, Eq, Hash, Clone)]
pub enum Event {
    Load,
    Save,
}

/// A subscriber (listener) has type of a callable function.
pub type Subscriber = fn(file_path: String);

/// Publisher sends events to subscribers (listeners).
#[derive(Default)]
pub struct Publisher {
    events: HashMap<Event, Vec<Subscriber>>,
}

impl Publisher {
    pub fn subscribe(&mut self, event_type: Event, listener: Subscriber) {
        self.events.entry(event_type.clone()).or_default();
        self.events.get_mut(&event_type).unwrap().push(listener);
    }

    pub fn unsubscribe(&mut self, event_type: Event, listener: Subscriber) {
        self.events
            .get_mut(&event_type)
            .unwrap()
            .retain(|&x| x != listener);
    }

    pub fn notify(&self, event_type: Event, file_path: String) {
        let listeners = self.events.get(&event_type).unwrap();
        for listener in listeners {
            listener(file_path.clone());
        }
    }
}
