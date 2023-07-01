pub trait UserRepository {
    fn find(&self) -> &[String];
    fn save(&mut self, date: String);
}

pub struct ImplRepository {
    list: Vec<String>,
}

impl ImplRepository {
    pub fn new() -> ImplRepository {
        return ImplRepository { list: Vec::new() };
    }
}

impl UserRepository for ImplRepository {
    fn save(&mut self, date: String) {
        self.list.push(date)
    }
    fn find(&self) -> &[String] {
        return &self.list;
    }
}
